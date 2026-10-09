"""Promote only pinned installer CI packages to an existing draft release.

No artifact code is imported or executed. Private API authorization is never
sent to redirects. Release publication and update feeds are outside this tool.
"""
from __future__ import annotations

import ast
import base64
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile

PUBLIC = "FadedMods/faded-mod-installer-cloud"
PRIVATE = "FadedMods/faded-local-mod-installer"
HEAD = "31190ecdfcbaef7f94716569f17d62060efd76b7"
TAG = "faded-local-mod-installer-0.3.9"
DRAFT_RELEASE_ID = 407444817
VERSION = "0.3.9"
PREFIX = "FadedLocalModInstaller-0.3.9-"
MODULES = tuple("app.pzf3d_" + name for name in
                ("access", "bootstrap", "config", "credentials", "github", "install",
                 "launcher", "release", "startup", "ui"))
GUIDE_SHA = "6f602c5fb54a97a73b2af3ea19355f9552708736ea4b559d0fbbec4a34d38d32"
MAX_ARCHIVE = 900 * 1024 * 1024
MAX_MEMBER = 800 * 1024 * 1024
MAX_TOTAL = 3 * 1024 * 1024 * 1024
SPECS = (
    (37876370271, "FadedLocalModInstaller-linux-standard-x86_64", "standard",
     (PREFIX + "linux-standard-x86_64.tar.gz",)),
    (37876370271, "FadedLocalModInstaller-linux-steamdeck-x86_64", "steamdeck",
     (PREFIX + "linux-x86_64.tar.gz",)),
    (37876372783, "FadedLocalModInstaller-macos-arm64", "arm64",
     (PREFIX + "macos-arm64.zip", PREFIX + "macos-arm64.dmg")),
    (37876372783, "FadedLocalModInstaller-macos-x86_64", "x86_64",
     (PREFIX + "macos-x86_64.zip", PREFIX + "macos-x86_64.dmg")),
)
PAYLOADS = frozenset(name for _, _, _, names in SPECS for name in names)


class PromotionError(RuntimeError):
    """Only fixed, nonsecret diagnostic messages may enter this exception."""


class ApiError(PromotionError):
    def __init__(self, status, route):
        self.status = status
        super().__init__("GitHub API " + route + " failed, HTTP " + str(status))


def need(value, message):
    if not value:
        raise PromotionError(message)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


HTTP = urllib.request.build_opener(NoRedirect())


def api(path, token, *, redirect=False, route="fixed-route"):
    need(path.startswith("/repos/"), "Invalid fixed API route")
    request = urllib.request.Request("https://api.github.com" + path, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "FadedMods-installer-native-promotion",
    })
    try:
        with HTTP.open(request, timeout=60) as response:
            need(not redirect and response.status == 200, "Unexpected API response")
            raw = response.read(4 * 1024 * 1024 + 1)
            need(len(raw) <= 4 * 1024 * 1024, "API response exceeds bound")
            return json.loads(raw)
    except urllib.error.HTTPError as failure:
        if redirect and failure.code in (301, 302, 303, 307, 308):
            location = failure.headers.get("Location", "")
            failure.close()
            need(bool(location), "Artifact redirect has no location")
            return location
        status = failure.code
        failure.close()
        raise ApiError(status, route) from None
    except (urllib.error.URLError, TimeoutError):
        raise PromotionError("GitHub API connection failed") from None


def cdn_allowed(url):
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    return (parsed.scheme == "https" and parsed.username is None and parsed.password is None
            and parsed.port in (None, 443) and not parsed.fragment and
            (host == "objects.githubusercontent.com"
             or re.fullmatch(r"productionresultssa[0-9a-z]+\.blob\.core\.windows\.net", host)
             or re.fullmatch(r"[a-z0-9-]+\.actions\.githubusercontent\.com", host)))


def download_artifact(artifact, token, target):
    size = artifact["size_in_bytes"]
    need(type(size) is int and 0 < size <= MAX_ARCHIVE, "Artifact size exceeds bound")
    digest = artifact.get("digest", "")
    need(re.fullmatch(r"sha256:[0-9a-f]{64}", digest) is not None,
         "Artifact API SHA256 digest is required")
    url = api(f"/repos/{PRIVATE}/actions/artifacts/{artifact['id']}/zip", token, redirect=True)
    for _ in range(5):
        need(cdn_allowed(url), "Artifact redirect is outside the HTTPS GitHub CDN allowlist")
        # Deliberately fresh request: no Authorization, cookie or private API headers.
        request = urllib.request.Request(url, headers={"User-Agent": "FadedMods-installer-native-promotion"})
        try:
            response = HTTP.open(request, timeout=120)
            break
        except urllib.error.HTTPError as failure:
            if failure.code in (301, 302, 303, 307, 308):
                url = urllib.parse.urljoin(url, failure.headers.get("Location", ""))
                failure.close()
                continue
            raise PromotionError("Artifact CDN request failed, HTTP " + str(failure.code)) from None
        except (urllib.error.URLError, TimeoutError):
            raise PromotionError("Artifact CDN connection failed") from None
    else:
        raise PromotionError("Artifact CDN redirect limit exceeded")
    hashed = hashlib.sha256()
    count = 0
    with response, target.open("xb") as output:
        need(response.status == 200, "Unexpected artifact CDN status")
        while block := response.read(1024 * 1024):
            count += len(block)
            need(count <= size and count <= MAX_ARCHIVE, "Artifact download exceeds declared size")
            hashed.update(block)
            output.write(block)
    need(count == size and hashed.hexdigest() == digest[7:], "Artifact archive size/SHA256 mismatch")
    return {"id": artifact["id"], "name": artifact["name"], "bytes": count,
            "sha256": hashed.hexdigest()}


def source_hashes(token):
    paths = [name.replace(".", "/") + ".py" for name in MODULES] + ["app/version.py"]
    def fetch(path):
        obj = api(f"/repos/{PRIVATE}/contents/{path}?ref={HEAD}", token)
        need(obj.get("encoding") == "base64", "Pinned source encoding unavailable")
        raw = base64.b64decode(obj["content"], validate=False)
        need(len(raw) <= 1024 * 1024, "Pinned source exceeds bound")
        if path == "app/version.py":
            tree = ast.parse(raw)
            versions = [node.value.value for node in tree.body
                        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant)
                        and any(isinstance(t, ast.Name) and t.id == "APP_VERSION" for t in node.targets)]
            need(versions == [VERSION], "Pinned source is not installer0.3.9")
        return path, hashlib.sha256(raw).hexdigest()
    with ThreadPoolExecutor(max_workers=6) as pool:
        return dict(pool.map(fetch, paths))


def proof_ok(raw, variant, hashes):
    need(len(raw) <= 1024 * 1024, "Native proof exceeds bound")
    proof = json.loads(raw)
    # version is the proof schema version, NOT the installer version.
    need(proof.get("schema") == "faded-installer-native-bundle-proof"
         and type(proof.get("version")) is int and proof["version"] == 1
         and proof.get("passed") is True, "Native bundle proof did not pass schema1")
    modules = proof.get("modules", {})
    need(isinstance(modules, dict) and set(modules) == set(MODULES),
         "Native proof must include all ten modules including app.pzf3d_access")
    for module in MODULES:
        row = modules[module]
        need(isinstance(row, dict) and row.get("frozenCodeMatchesSource") is True
             and row.get("sourceSha256") == hashes[module.replace(".", "/") + ".py"]
             and re.fullmatch(r"[0-9a-f]{64}", row.get("bytecodeSha256", "")) is not None,
             "Native frozen/source module proof mismatch")
    assets = proof.get("assets", {})
    need(isinstance(assets, dict) and "pzf3d-publisher.json" in assets
         and assets.get("pzf3d/PZ-F3D-Player-Guide.pdf", {}).get("sha256") == GUIDE_SHA,
         "Native proof misses approved resources")
    for row in assets.values():
        need(isinstance(row, dict) and re.fullmatch(r"[0-9a-f]{64}", row.get("sha256", ""))
             and row.get("sha256") == row.get("packagedSha256")
             and type(row.get("size")) is int and row["size"] > 0,
             "Native resource proof mismatch")
    need(proof.get("cliHelp", {}).get("exitCode") == 0, "Native frozen CLI proof failed")
    if variant in ("arm64", "x86_64"):
        need(proof.get("machine") == variant, "Native macOS architecture proof mismatch")
    else:
        need(proof.get("machine") == "x86_64", "Native Linux architecture proof mismatch")
    return {"variant": variant, "schema": proof["schema"], "schemaVersion": 1,
            "passed": True, "proofSha256": hashlib.sha256(raw).hexdigest(),
            "modules": modules, "assetCount": len(assets), "cliExitCode": 0}


def inspect_and_extract(archive, spec, destination, hashes):
    _, _, variant, names = spec
    proof_name = "pzf3d-native-proof-" + variant + ".json"
    allowed = set(names) | {proof_name}
    if variant in ("arm64", "x86_64"):
        allowed.add(PREFIX + "macos-" + variant + ".sha256")
    members = {}
    with zipfile.ZipFile(archive) as package:
        infos = package.infolist()
        need(0 < len(infos) <= 32, "Artifact ZIP entry count exceeds bound")
        total = 0
        seen_paths = set()
        for info in infos:
            name = info.filename
            need(name not in seen_paths and "\\" not in name and ":" not in name
                 and "\0" not in name and not name.startswith("/")
                 and all(part not in ("", ".", "..") for part in name.rstrip("/").split("/")),
                 "Unsafe or duplicate artifact ZIP path")
            seen_paths.add(name)
            mode = info.external_attr >> 16
            kind = stat.S_IFMT(mode)
            need(not info.flag_bits & 1 and kind in (0, stat.S_IFREG, stat.S_IFDIR)
                 and (not info.is_dir() or info.file_size == 0), "ZIP links/special/encrypted entries refused")
            if info.is_dir():
                continue
            base = name.rsplit("/", 1)[-1]
            need(base in allowed and base not in members, "Unexpected/ambiguous artifact member")
            limit = MAX_MEMBER if base in names else 1024 * 1024
            need(0 < info.file_size <= limit and info.compress_size > 0
                 and info.file_size <= info.compress_size * 200, "Artifact ZIP expansion bound exceeded")
            total += info.file_size
            need(total <= MAX_TOTAL, "Artifact ZIP total exceeds bound")
            members[base] = info
        need(set(names) <= set(members) and proof_name in members, "Expected native payload/proof missing")
        proof = proof_ok(package.read(members[proof_name]), variant, hashes)
        payloads = []
        # No extractall: only these six fixed basenames may reach the filesystem.
        for name in names:
            info = members[name]
            hashed = hashlib.sha256()
            count = 0
            target = destination / name
            with package.open(info) as source, target.open("xb") as output:
                while block := source.read(1024 * 1024):
                    count += len(block)
                    need(count <= info.file_size, "Native payload exceeds declared ZIP size")
                    hashed.update(block)
                    output.write(block)
            need(count == info.file_size, "Native payload ZIP size mismatch")
            payloads.append({"fileName": name, "bytes": count, "sha256": hashed.hexdigest()})
    return proof, payloads


def release(token):
    # Pin the already-created draft by ID. Untagged drafts have no tag endpoint,
    # and this repository contains more than five hundred historical releases.
    value = api(f"/repos/{PUBLIC}/releases/{DRAFT_RELEASE_ID}", token, route="fixed-draft-id")
    need(isinstance(value, dict) and value.get("tag_name") == TAG
         and value.get("draft") is True and type(value.get("id")) is int
         and value["id"] == DRAFT_RELEASE_ID,
         "Existing installer0.3.9 DRAFT release required")
    return value


def main():
    need(len(sys.argv) == 1, "This fixed promotion accepts no arguments")
    need(os.environ.get("GITHUB_REPOSITORY") == PUBLIC
         and os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch",
         "Promotion requires the fixed public repository manual workflow")
    token = os.environ.get("GH_TOKEN", "")
    need(bool(token), "Required server credential unavailable")
    checked = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    need(re.fullmatch(r"[0-9a-f]{40}", checked) and checked == os.environ.get("GITHUB_SHA"),
         "Checkout must match immutable dispatch GitHub SHA")
    repo = api(f"/repos/{PUBLIC}", token, route="public-repository")
    need(os.environ.get("GITHUB_REF") == "refs/heads/" + repo["default_branch"],
         "Promotion may run only from the default branch")
    receipt_dir = Path("native-promotion-receipt")
    receipt_dir.mkdir(exist_ok=False)
    receipt = {"schema": "faded-installer-native-artifact-promotion", "version": 1,
               "installerVersion": VERSION, "sourceRepository": PRIVATE, "sourceCommit": HEAD,
               "publicRepository": PUBLIC, "releaseTag": TAG, "workflowCommit": checked,
               "startedUtc": datetime.now(timezone.utc).isoformat(), "passed": False,
               "releasePublished": False, "feedChanged": False, "overwriteAllowed": False,
               "phase": "draft-preflight", "artifacts": [], "proofs": [], "packages": []}
    try:
        initial = release(token)
        need(not PAYLOADS.intersection(a["name"] for a in initial.get("assets", [])),
             "A requested release asset already exists; no overwrite permitted")
        receipt["phase"] = "ci-provenance"
        all_artifacts = {}
        for run in sorted({s[0] for s in SPECS}):
            status = api(f"/repos/{PRIVATE}/actions/runs/{run}", token)
            need(status.get("id") == run and status.get("status") == "completed"
                 and status.get("conclusion") == "success" and status.get("head_sha") == HEAD
                 and status.get("event") == "workflow_dispatch"
                 and status.get("repository", {}).get("full_name") == PRIVATE
                 and status.get("head_repository", {}).get("full_name") == PRIVATE,
                 "Pinned CI run must be completed SUCCESS at exact approved source")
            listing = api(f"/repos/{PRIVATE}/actions/runs/{run}/artifacts?per_page=100", token)
            expected = {s[1] for s in SPECS if s[0] == run}
            rows = listing.get("artifacts", [])
            need(listing.get("total_count") == len(expected) == len(rows)
                 and {a.get("name") for a in rows} == expected, "CI artifact roster mismatch")
            for artifact in rows:
                provenance = artifact.get("workflow_run", {})
                need(artifact.get("expired") is False and type(artifact.get("id")) is int
                     and provenance.get("id") == run and provenance.get("head_sha") == HEAD,
                     "CI artifact is expired or has wrong provenance")
                all_artifacts[artifact["name"]] = artifact
        need(sum(a["size_in_bytes"] for a in all_artifacts.values()) <= MAX_TOTAL,
             "Combined artifacts exceed download budget")
        receipt["phase"] = "pinned-source"
        hashes = source_hashes(token)
        receipt["pinnedSourceSha256"] = hashes
        with tempfile.TemporaryDirectory(prefix="pzf3d-native-promotion-") as temp:
            scratch = Path(temp)
            payload_dir = scratch / "payloads"
            payload_dir.mkdir()
            def prepare(spec):
                artifact = all_artifacts[spec[1]]
                archive = scratch / (str(artifact["id"]) + ".zip")
                metadata = download_artifact(artifact, token, archive)
                proof, packages = inspect_and_extract(archive, spec, payload_dir, hashes)
                return metadata, proof, packages
            receipt["phase"] = "artifact-download-validation"
            with ThreadPoolExecutor(max_workers=4) as pool:
                for metadata, proof, packages in pool.map(prepare, SPECS):
                    receipt["artifacts"].append(metadata)
                    receipt["proofs"].append(proof)
                    receipt["packages"].extend(packages)
            need({p["fileName"] for p in receipt["packages"]} == PAYLOADS
                 and len(receipt["packages"]) == 6, "Exact six native packages required")
            receipt["phase"] = "draft-recheck"
            before = release(token)
            need(before["id"] == initial["id"]
                 and not PAYLOADS.intersection(a["name"] for a in before.get("assets", [])),
                 "Draft release changed or target asset appeared before upload")
            command = ["gh", "release", "upload", TAG,
                       *(str(payload_dir / name) for name in sorted(PAYLOADS)), "--repo", PUBLIC]
            # Fixed file list; no --clobber, release creation, publication or feed command.
            receipt["phase"] = "upload"
            result = subprocess.run(command, capture_output=True, text=True, timeout=1800)
            receipt["uploadExitCode"] = result.returncode
            need(result.returncode == 0, "gh release upload failed; inspect draft assets before retry")
            receipt["phase"] = "uploaded-verification"
            after = release(token)
            need(after["id"] == initial["id"], "Draft release identity changed")
            remote = {a["name"]: a for a in after.get("assets", [])}
            for row in receipt["packages"]:
                asset = remote.get(row["fileName"], {})
                need(asset.get("state") == "uploaded" and asset.get("size") == row["bytes"],
                     "Uploaded native release asset size/state mismatch")
                digest = asset.get("digest")
                need(digest is None or digest == "sha256:" + row["sha256"],
                     "Uploaded native release asset SHA256 mismatch")
                row["releaseAssetId"] = asset["id"]
                row["githubDigest"] = digest
        receipt["passed"] = True
        receipt["phase"] = "complete"
    except Exception as failure:
        receipt["failureType"] = type(failure).__name__
        if isinstance(failure, PromotionError):
            receipt["failure"] = str(failure)
        raise
    finally:
        receipt["finishedUtc"] = datetime.now(timezone.utc).isoformat()
        (receipt_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        (receipt_dir / "SHA256SUMS.txt").write_text(
            "".join(p["sha256"] + "  " + p["fileName"] + "\n" for p in receipt["packages"]), encoding="utf-8")
        summary = "Native installer promotion: " + ("PASS" if receipt["passed"] else "FAIL") + "\n\n"
        summary += "Phase: " + receipt["phase"] + "\n\n"
        summary += "Draft remains unpublished; feed unchanged; no overwrite.\n\n"
        summary += "\n".join(p["fileName"] + " | " + str(p["bytes"]) + " bytes | " + p["sha256"]
                             for p in receipt["packages"]) + "\n"
        (receipt_dir / "summary.txt").write_text(summary, encoding="utf-8")
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as output:
                output.write(summary)
        print(summary)


if __name__ == "__main__":
    try:
        main()
    except Exception as failure:
        # Never print urllib/subprocess exceptions, signed CDN URLs or credentials.
        message = str(failure) if isinstance(failure, PromotionError) else type(failure).__name__
        print("Native promotion failed: " + message, file=sys.stderr)
        sys.exit(1)
