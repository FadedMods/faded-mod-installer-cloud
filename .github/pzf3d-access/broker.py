"""Fixed-release encrypted ticket broker. Credentials never leave GitHub API.

This file is intended to run from a trusted, pinned default-branch workflow.
It does not change repository permissions or accept client-selected resources.
"""
from __future__ import annotations

import base64
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PUBLIC_REPO = "FadedMods/faded-mod-installer-cloud"
PRIVATE_REPO = "FadedMods/pz-f3d-downloads"
PRIVATE_REPO_ID = 1409483562
TITLE = "PZ-F.3D automatic download access"
PREFIX = "PZF3D-TICKET-V1\n"
FAILURE = "PZF3D-ACCESS-ERROR-V1\nAutomatic download access could not be prepared. Please retry sign-in later."
API = "https://api.github.com"
CDN_HOSTS = frozenset({"release-assets.githubusercontent.com", "objects.githubusercontent.com"})
MAX_INT = 2**53 - 1
MAX_EVENT = 262144
MAX_BODY = 4096
MAX_JSON = 2097152
MAX_INLINE = 2097152
MAX_COMMENT = 65536
MAX_ASSETS = 64
TTL = 1800


class BrokerError(Exception):
    """Deliberately does not carry upstream bodies, credentials or URLs."""


def fail() -> None:
    raise BrokerError("Automatic download access could not be prepared.")


def positive(value: object) -> bool:
    return type(value) is int and 1 <= value <= MAX_INT


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            fail()
        result[key] = value
    return result


def parse_json(raw: bytes):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs,
                          parse_constant=lambda _: fail())
    except (ValueError, UnicodeError, RecursionError):
        fail()


def encoded(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


@dataclass(frozen=True)
class Request:
    issue_number: int
    login: str
    user_id: int
    nonce: str
    public_key: rsa.RSAPublicKey


def issue_number(event: object) -> int:
    """Only expose the fixed repository's issue number, before body validation."""
    if type(event) is not dict or event.get("action") != "opened":
        fail()
    repository = event.get("repository")
    issue = event.get("issue")
    if (type(repository) is not dict or repository.get("full_name") != PUBLIC_REPO
            or repository.get("private") is not False or type(issue) is not dict
            or issue.get("title") != TITLE or issue.get("state") != "open"
            or "pull_request" in issue or not positive(issue.get("number"))):
        fail()
    return issue["number"]


def validate_request(event: object) -> Request:
    number = issue_number(event)
    issue = event["issue"]
    author = issue.get("user")
    if type(author) is not dict or author.get("type") != "User" or not positive(author.get("id")):
        fail()
    login = author.get("login")
    if type(login) is not str or not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", login):
        fail()
    body = issue.get("body")
    if type(body) is not str or len(body.encode("utf-8")) > MAX_BODY:
        fail()
    request = parse_json(body.encode("utf-8"))
    if (type(request) is not dict or set(request) != {"schema", "nonce", "publicKey"}
            or type(request["schema"]) is not int or request["schema"] != 1
            or type(request["nonce"]) is not str or not re.fullmatch(r"[0-9a-f]{64}", request["nonce"])):
        fail()
    pem = request["publicKey"]
    if type(pem) is not str or not 1 <= len(pem) <= 2048 or not pem.isascii():
        fail()
    try:
        key = serialization.load_pem_public_key(pem.encode("ascii"))
    except (ValueError, TypeError):
        fail()
    if not isinstance(key, rsa.RSAPublicKey) or key.key_size != 2048 or key.public_numbers().e != 65537:
        fail()
    return Request(number, login, author["id"], request["nonce"], key)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


class Api:
    def __init__(self, public_token: str, private_token: str, *, opener=None):
        if not self.valid_token(public_token):
            fail()
        self.public_token = public_token
        self.private_token = private_token
        self.opener = opener or urllib.request.build_opener(NoRedirect(), urllib.request.HTTPSHandler(context=ssl.create_default_context()))

    @staticmethod
    def valid_token(token: object) -> bool:
        return type(token) is str and 1 <= len(token) <= 4096 and token.isascii() and not any(c.isspace() for c in token)

    def request(self, method: str, path: str, *, private: bool, body=None, binary=False):
        # Token destination and resource scope are fixed independently of event data.
        prefix = "/repos/" + (PRIVATE_REPO if private else PUBLIC_REPO)
        if not path.startswith(prefix + "/") and path != prefix:
            fail()
        if any(c in path for c in ("?", "#", "\\", "\r", "\n")) or ".." in path:
            fail()
        if private and (not self.valid_token(self.private_token) or method != "GET" or body is not None
                        or not (path == prefix or path == prefix + "/releases/latest"
                                or re.fullmatch(re.escape(prefix) + r"/releases/assets/[1-9][0-9]{0,15}", path))):
            fail()
        headers = {"Accept": "application/octet-stream" if binary else "application/vnd.github+json",
                   "Authorization": "Bearer " + (self.private_token if private else self.public_token),
                   "User-Agent": "Faded-PZF3D-Access-Broker", "X-GitHub-Api-Version": "2022-11-28",
                   "Cache-Control": "no-cache"}
        data = None
        if body is not None:
            data = encoded(body)
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(API + path, data=data, headers=headers, method=method)
        try:
            return self.opener.open(request, timeout=25)
        except urllib.error.HTTPError as response:
            return response
        except (OSError, ValueError):
            fail()

    def json(self, method: str, path: str, *, private: bool, body=None, expected=200):
        with self.request(method, path, private=private, body=body) as response:
            if response.status != expected:
                fail()
            if expected == 204:
                return None
            raw = response.read(MAX_JSON + 1)
            if len(raw) > MAX_JSON:
                fail()
        data = parse_json(raw)
        if type(data) is not dict:
            fail()
        return data

    def comment(self, number: int, body: str):
        if not positive(number) or len(body) > MAX_COMMENT:
            fail()
        return self.json("POST", f"/repos/{PUBLIC_REPO}/issues/{number}/comments", private=False,
                         body={"body": body}, expected=201)

    def close(self, number: int):
        if not positive(number):
            fail()
        return self.json("PATCH", f"/repos/{PUBLIC_REPO}/issues/{number}", private=False, body={"state": "closed"})


def valid_cdn_url(url: object) -> bool:
    if type(url) is not str or not 1 <= len(url) <= 8192 or any(ord(c) <= 32 or ord(c) == 127 for c in url):
        return False
    try:
        parsed = urllib.parse.urlsplit(url)
        return (parsed.scheme == "https" and parsed.hostname in CDN_HOSTS
                and parsed.port in (None, 443) and parsed.username is None
                and parsed.password is None and not parsed.fragment and bool(parsed.path))
    except ValueError:
        return False


def asset_ticket(api: Api, asset: dict) -> dict:
    asset_id, size, name = asset.get("id"), asset.get("size"), asset.get("name")
    if (not positive(asset_id) or not positive(size) or size > 80 * 1024**3
            or type(name) is not str or not 1 <= len(name) <= 256
            or any(ord(c) < 32 or ord(c) == 127 for c in name)):
        fail()
    with api.request("GET", f"/repos/{PRIVATE_REPO}/releases/assets/{asset_id}", private=True, binary=True) as response:
        if response.status in (302, 307):
            url = response.headers.get("Location")
            if not valid_cdn_url(url):
                fail()
            return {"url": url, "size": size, "name": name}
        if response.status == 200 and size <= MAX_INLINE:
            raw = response.read(min(MAX_INLINE, size) + 1)
            if len(raw) != size:
                fail()
            return {"data": base64.b64encode(raw).decode("ascii"), "size": size, "name": name}
        fail()


def build_ticket(api: Api, request: Request, *, now: int | None = None) -> dict:
    repository = api.json("GET", "/repos/" + PRIVATE_REPO, private=True)
    if (repository.get("id") != PRIVATE_REPO_ID or type(repository.get("id")) is not int
            or repository.get("full_name") != PRIVATE_REPO or repository.get("private") is not True):
        fail()
    release = api.json("GET", f"/repos/{PRIVATE_REPO}/releases/latest", private=True)
    if (not positive(release.get("id")) or release.get("draft") is not False or release.get("prerelease") is not False
            or type(release.get("tag_name")) is not str or not 1 <= len(release["tag_name"]) <= 128
            or type(release.get("published_at")) is not str or not release["published_at"]
            or type(release.get("assets")) is not list or not 1 <= len(release["assets"]) <= MAX_ASSETS):
        fail()
    assets = {}
    total = 0
    for asset in release["assets"]:
        if type(asset) is not dict or not positive(asset.get("id")) or str(asset["id"]) in assets:
            fail()
        entry = asset_ticket(api, asset)
        total += entry["size"]
        if total > 80 * 1024**3:
            fail()
        assets[str(asset["id"])] = entry
    issued = int(time.time()) if now is None else now
    if not positive(issued) or issued > MAX_INT - TTL:
        fail()
    return {"schema": 1, "nonce": request.nonce, "login": request.login, "userId": request.user_id,
            "repository": PRIVATE_REPO, "repositoryId": PRIVATE_REPO_ID,
            "issuedAt": issued, "expiresAt": issued + TTL, "release": release, "assets": assets}


def encrypt_ticket(request: Request, ticket: dict) -> str:
    plaintext = encoded(ticket)
    # Ciphertext/base64/RSA/envelope overhead must fit GitHub's comment boundary.
    if len(plaintext) > 48000:
        fail()
    key = AESGCM.generate_key(bit_length=256)
    iv = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(iv, plaintext, request.nonce.encode("utf-8"))
    encrypted_key = request.public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                               algorithm=hashes.SHA256(), label=None))
    envelope = {"schema": 1, "nonce": request.nonce, "key": base64.b64encode(encrypted_key).decode("ascii"),
                "ciphertext": base64.b64encode(ciphertext).decode("ascii"), "iv": base64.b64encode(iv).decode("ascii")}
    comment = PREFIX + encoded(envelope).decode("utf-8")
    if len(comment) > MAX_COMMENT:
        fail()
    return comment


def process_event(event: object, api: Api, *, now=None) -> bool:
    number = issue_number(event)
    try:
        request = validate_request(event)
        comment = encrypt_ticket(request, build_ticket(api, request, now=now))
        api.comment(number, comment)
    except Exception:
        # Never include exception text, upstream headers/bodies or CDN URLs.
        api.comment(number, FAILURE)
        api.close(number)
        return False
    api.close(number)
    return True


def main() -> int:
    try:
        event_path = Path(os.environ["GITHUB_EVENT_PATH"])
        with event_path.open("rb") as source:
            raw = source.read(MAX_EVENT + 1)
        if len(raw) > MAX_EVENT:
            fail()
        event = parse_json(raw)
        # Ignore ordinary public issues without touching private resources.
        try:
            issue_number(event)
        except BrokerError:
            return 0
        api = Api(os.environ["GITHUB_TOKEN"], os.environ.get("PZF3D_DOWNLOAD_BROKER_TOKEN", ""))
        if not process_event(event, api):
            print("Automatic download access request failed; a redacted status was posted.")
            return 1
        print("Encrypted download ticket posted; repository permissions unchanged.")
        return 0
    except Exception:
        print("Automatic download access broker failed; details withheld.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
