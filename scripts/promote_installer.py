"""Stage six exact-source installer CI packages in a pre-existing cloud draft.

The existing broker credential authorizes private GET requests only. Cloud
release uploads use GITHUB_TOKEN. No downloaded code is imported or executed.
"""
from __future__ import annotations
import ast
import base64
from concurrent.futures import ThreadPoolExecutor
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import struct
import subprocess
import tarfile
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from promote_native import NoRedirect, PromotionError, cdn_allowed, need

PUBLIC = "FadedMods/faded-mod-installer-cloud"
PRIVATE = "FadedMods/faded-local-mod-installer"
VERSION = "0.3.25"
TAG = "faded-local-mod-installer-" + VERSION
PREFIX = "FadedLocalModInstaller-" + VERSION + "-"
APPROVED_BRANCH = "refs/heads/release/installer-0.3.25-smapi"
MAX_ARTIFACT = 900 * 1024**2
MAX_TOTAL = 3 * 1024**3
EDITIONS = {
    "windows": ("windows", "Windows windows", "FadedLocalModInstaller-windows", "windows"),
    "windows-multilingual": ("windows", "Windows windows-multilingual", "FadedLocalModInstaller-windows-multilingual", "windows-multilingual"),
    "linux-standard": ("linux", "Linux standard", "FadedLocalModInstaller-linux-standard-x86_64", "standard"),
    "linux-steamdeck": ("linux", "Linux steamdeck", "FadedLocalModInstaller-linux-steamdeck-x86_64", "steamdeck"),
    "macos-arm64": ("macos", "macOS arm64", "FadedLocalModInstaller-macos-arm64", "arm64"),
    "macos-x86_64": ("macos", "macOS x86_64", "FadedLocalModInstaller-macos-x86_64", "x86_64"),
}
HTTP = urllib.request.build_opener(NoRedirect())


def api(path, *, private=True, redirect=False):
    repository = PRIVATE if private else PUBLIC
    need(path.startswith("/repos/" + repository + "/"), "Fixed API repository boundary")
    request = urllib.request.Request("https://api.github.com" + path, method="GET", headers={
        "Authorization": "Bearer " + os.environ["SOURCE_READ_TOKEN" if private else "GH_TOKEN"],
        "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Faded-installer-native-promotion",
    })
    try:
        with HTTP.open(request, timeout=90) as response:
            need(not redirect and response.status == 200, "Unexpected API response")
            raw = response.read(64 * 1024**2 + 1)
            need(len(raw) <= 64 * 1024**2, "API metadata bound")
            return json.loads(raw)
    except urllib.error.HTTPError as error:
        if redirect and error.code in (301, 302, 303, 307, 308):
            location = error.headers.get("Location", "")
            error.close()
            need(bool(location), "Artifact redirect missing")
            return location
        status = error.code
        error.close()
        raise PromotionError("Fixed GitHub API request failed, HTTP " + str(status)) from None
    except (urllib.error.URLError, TimeoutError):
        raise PromotionError("Fixed GitHub API connection failed") from None


def digest(path):
    hashed = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024**2), b""):
            hashed.update(block)
    return hashed.hexdigest()


def source_blob(path, source):
    row = api(f"/repos/{PRIVATE}/contents/{path}?ref={source}")
    need(row.get("encoding") == "base64", "Pinned source encoding unavailable")
    return base64.b64decode(row["content"])


def pinned_source(source):
    verifier = ast.parse(source_blob("scripts/verify_pzf3d_bundle.py", source))
    values = {node.targets[0].id: ast.literal_eval(node.value) for node in verifier.body
              if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
              and node.targets[0].id in {"MODULES", "RESOURCE_SUFFIXES", "APP_VERSION"}}
    modules = values["MODULES"]
    need(values["APP_VERSION"] == VERSION and len(modules) == 23 and "app.stardew_smapi" in modules
         and all(re.fullmatch(r"app\.[a-z0-9_]+", name) for name in modules), "Pinned native module contract")
    def module_hash(name):
        raw = source_blob(name.replace(".", "/") + ".py", source)
        if name == "app.version":
            actual = {target.id: ast.literal_eval(node.value) for node in ast.parse(raw).body if isinstance(node, ast.Assign)
                      for target in node.targets if isinstance(target, ast.Name)}
            need(actual.get("APP_VERSION") == actual.get("__version__") == VERSION, "Pinned application version")
        return name, hashlib.sha256(raw).hexdigest()
    with ThreadPoolExecutor(max_workers=8) as pool:
        module_hashes = dict(pool.map(module_hash, modules))
    commit = api(f"/repos/{PRIVATE}/git/commits/{source}")
    need(commit.get("sha") == source, "Pinned source commit")
    tree = api(f"/repos/{PRIVATE}/git/trees/{commit['tree']['sha']}?recursive=1")
    need(tree.get("truncated") is False and tree.get("sha") == commit["tree"]["sha"], "Pinned complete Git tree")
    assets = [row for row in tree["tree"] if row["type"] == "blob" and row["path"].startswith("app/assets/")
              and Path(row["path"]).suffix.lower() in values["RESOURCE_SUFFIXES"]]
    need(len(assets) == 30 and sum(row["size"] for row in assets) <= 128 * 1024**2, "Pinned resource bounds")
    def asset_hash(row):
        blob = api(f"/repos/{PRIVATE}/git/blobs/{row['sha']}")
        need(blob.get("encoding") == "base64", "Pinned resource encoding")
        raw = base64.b64decode(blob["content"])
        need(len(raw) == row["size"] and hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == row["sha"], "Pinned resource Git identity")
        return row["path"][len("app/assets/"):], dict(size=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    with ThreadPoolExecutor(max_workers=8) as pool:
        return module_hashes, dict(pool.map(asset_hash, assets))


def download(artifact, path):
    need(type(artifact["size_in_bytes"]) is int and 0 < artifact["size_in_bytes"] <= MAX_ARTIFACT
         and re.fullmatch(r"sha256:[a-f0-9]{64}", artifact.get("digest", "")), "Artifact size/digest metadata")
    url = api(f"/repos/{PRIVATE}/actions/artifacts/{artifact['id']}/zip", redirect=True)
    for _ in range(5):
        need(cdn_allowed(url), "Artifact redirect outside GitHub storage")
        request = urllib.request.Request(url, headers={"User-Agent": "Faded-installer-native-promotion"})
        try:
            response = HTTP.open(request, timeout=180)
            break
        except urllib.error.HTTPError as error:
            if error.code in (301, 302, 303, 307, 308):
                url = urllib.parse.urljoin(url, error.headers.get("Location", ""))
                error.close()
                continue
            status = error.code
            error.close()
            raise PromotionError("Artifact storage request failed, HTTP " + str(status)) from None
        except (urllib.error.URLError, TimeoutError):
            raise PromotionError("Artifact storage connection failed") from None
    else:
        raise PromotionError("Artifact storage redirect limit")
    count, hashed = 0, hashlib.sha256()
    with response, path.open("xb") as output:
        need(response.status == 200, "Artifact storage response")
        while block := response.read(1024**2):
            count += len(block)
            need(count <= artifact["size_in_bytes"], "Artifact transfer size exceeded")
            hashed.update(block)
            output.write(block)
    need(count == artifact["size_in_bytes"] and "sha256:" + hashed.hexdigest() == artifact["digest"], "Artifact transfer digest mismatch")


def package_names(edition):
    if edition.startswith("windows"):
        return [PREFIX + edition + ".zip"]
    if edition.startswith("linux"):
        return [PREFIX + ("linux-standard-x86_64" if edition == "linux-standard" else "linux-x86_64") + ".tar.gz"]
    return [PREFIX + edition + suffix for suffix in (".zip", ".dmg", ".sha256")]


def native_payload(path, edition, proof):
    if edition.startswith("linux"):
        relative, executable = "app/faded-local-mod-installer", None
        with gzip.open(path, "rb") as stream:
            with tarfile.open(fileobj=stream, mode="r|") as bundle:
                for member in bundle:
                    if member.name == relative or member.name.endswith("/" + relative):
                        need(executable is None and member.isfile() and member.size <= MAX_ARTIFACT, "Unique native Linux executable")
                        executable = bundle.extractfile(member).read()
            while stream.read(1024**2):
                pass
        need(executable is not None and executable[:6] == b"\x7fELF\x02\x01" and struct.unpack_from("<H", executable, 18)[0] == 62, "Native Linux architecture")
    else:
        relative = ("Faded Local Mod Installer" + (" Multilingual" if edition == "windows-multilingual" else "") + ".exe"
                    if edition.startswith("windows") else "Faded Local Mod Installer.app/Contents/MacOS/Faded Local Mod Installer")
        with zipfile.ZipFile(path) as bundle:
            need(bundle.testzip() is None, "Native ZIP CRC")
            names = [name for name in bundle.namelist() if name == relative or name.endswith("/" + relative)]
            need(len(names) == 1, "Unique native ZIP executable")
            executable = bundle.read(names[0])
        if edition.startswith("windows"):
            need(executable[:2] == b"MZ" and len(executable) >= 64, "Native Windows header")
            offset = struct.unpack_from("<I", executable, 60)[0]
            need(64 <= offset <= 1024**2 and executable[offset:offset + 4] == b"PE\0\0"
                 and struct.unpack_from("<H", executable, offset + 4)[0] == 0x8664
                 and struct.unpack_from("<H", executable, offset + 24)[0] == 0x20b, "Native Windows architecture")
        else:
            need(executable[:4] == b"\xcf\xfa\xed\xfe" and struct.unpack_from("<I", executable, 4)[0]
                 == (0x100000c if edition == "macos-arm64" else 0x1000007), "Native macOS architecture")
    need(hashlib.sha256(executable).hexdigest() == proof.get("executableSha256"), "Executable differs from native proof")
    return relative


def prepare(edition, artifact, folder, modules, assets, source, run):
    variant = EDITIONS[edition][3]
    proof_name = "pzf3d-native-proof-" + variant + ".json"
    names = package_names(edition)
    archive = folder / (edition + "-artifact.zip")
    download(artifact, archive)
    with zipfile.ZipFile(archive) as bundle:
        members = {}
        need(0 < len(bundle.infolist()) <= 32, "Artifact member count")
        for info in bundle.infolist():
            name = info.filename
            need(info.orig_filename == name and "\\" not in name and ":" not in name and not name.startswith("/")
                 and all(part not in ("", ".", "..") for part in name.rstrip("/").split("/")), "Artifact unsafe path")
            need(stat.S_IFMT(info.external_attr >> 16) in (0, stat.S_IFREG, stat.S_IFDIR) and not info.flag_bits & 1, "Artifact linked/encrypted member")
            if info.is_dir():
                continue
            base = name.rsplit("/", 1)[-1]
            need(base in {*names, proof_name} and base not in members and 0 < info.file_size <= MAX_ARTIFACT, "Artifact unexpected member")
            members[base] = info
        need(set(members) == {*names, proof_name}, "Exact artifact package/proof roster")
        need(members[proof_name].file_size <= 1024**2, "Native proof bound")
        proof = json.loads(bundle.read(members[proof_name]))
        need(proof.get("schema") == "faded-installer-native-bundle-proof" and type(proof.get("version")) is int
             and proof["version"] == 1 and proof.get("passed") is True and proof.get("appVersion") == VERSION, "Native proof contract/version")
        need(set(proof.get("modules", {})) == set(modules), "Native proof complete module roster")
        for name, expected in modules.items():
            row = proof["modules"][name]
            need(row.get("sourceSha256") == expected and row.get("frozenCodeMatchesSource") is True, "Native frozen module source binding")
        need(set(proof.get("assets", {})) == set(assets) and proof.get("assetsVerified") == len(assets)
             and proof.get("assetBytesReadFromFrozenBundle") is True, "Native complete packaged resource roster")
        for name, expected in assets.items():
            row = proof["assets"][name]
            need(row.get("sha256") == row.get("packagedSha256") == expected["sha256"] and row.get("size") == expected["size"], "Native packaged resource source binding")
        machine = {"amd64": "x86_64", "x64": "x86_64", "aarch64": "arm64"}.get(str(proof.get("machine", "")).lower(), str(proof.get("machine", "")).lower())
        need(machine == ("arm64" if edition == "macos-arm64" else "x86_64") and proof.get("cliHelp", {}).get("exitCode") == 0, "Native machine/CLI qualification")
        for name in names:
            with bundle.open(members[name]) as reader, (folder / name).open("xb") as writer:
                for block in iter(lambda: reader.read(1024**2), b""):
                    writer.write(block)
    archive.unlink()
    primary = next(folder / name for name in names if name.endswith(".tar.gz" if edition.startswith("linux") else ".zip"))
    relative = native_payload(primary, edition, proof)
    if edition.startswith("macos"):
        expected, listed = {name for name in names if name.endswith((".zip", ".dmg"))}, set()
        for line in (folder / next(name for name in names if name.endswith(".sha256"))).read_text().splitlines():
            checksum, name = line.split(maxsplit=1)
            name = name.strip().lstrip("*")
            need(name in expected and name not in listed and digest(folder / name) == checksum, "macOS package checksums")
            listed.add(name)
        need(listed == expected, "macOS checksum roster")
        with (folder / next(name for name in names if name.endswith(".dmg"))).open("rb") as stream:
            stream.seek(-512, 2)
            need(stream.read(4) == b"koly", "macOS DMG native trailer")
    proof["executable"] = relative
    proof["normalizedMachine"] = machine
    proof["publicationProvenance"] = dict(sourceCommit=source, workflowRun=f"https://github.com/{PRIVATE}/actions/runs/{run}",
                                           job=EDITIONS[edition][1], artifact=artifact["name"], executableAbsolutePathRedacted=True)
    proof_file = PREFIX + edition + "-bundle-proof.json"
    (folder / proof_file).write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return [dict(name=name, size=(folder / name).stat().st_size, sha256=digest(folder / name)) for name in [*names, proof_file]]


def main():
    source, release_id = os.environ.get("PROMOTION_SOURCE_SHA", ""), os.environ.get("PROMOTION_RELEASE_ID", "")
    need(re.fullmatch(r"[a-f0-9]{40}", source) and re.fullmatch(r"[1-9][0-9]{0,15}", release_id), "Source/release inputs")
    runs = {platform: os.environ.get("PROMOTION_" + platform.upper() + "_RUN", "") for platform in ("windows", "linux", "macos")}
    need(all(re.fullmatch(r"[1-9][0-9]{0,15}", value) for value in runs.values()), "CI run inputs")
    need(os.environ.get("GITHUB_REPOSITORY") == PUBLIC and os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch", "Fixed promotion repository/event")
    need(os.environ.get("GITHUB_REF") in {APPROVED_BRANCH, "refs/heads/main"}, "Approved promotion branch")
    checkout = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    need(checkout == os.environ.get("GITHUB_SHA") and os.environ.get("SOURCE_READ_TOKEN") and os.environ.get("GH_TOKEN"), "Immutable checkout and existing credentials required")
    def release():
        value = api(f"/repos/{PUBLIC}/releases/{release_id}", private=False)
        need(value.get("id") == int(release_id) and value.get("tag_name") == TAG and value.get("draft") is True, "Exact unpublished target draft required")
        return value
    release()
    selected = {}
    for platform, run in runs.items():
        metadata = api(f"/repos/{PRIVATE}/actions/runs/{run}")
        need(metadata.get("status") == "completed" and metadata.get("conclusion") == "success" and metadata.get("head_sha") == source
             and metadata.get("event") == "workflow_dispatch" and metadata.get("repository", {}).get("full_name") == PRIVATE
             and metadata.get("head_repository", {}).get("full_name") == PRIVATE, "Exact-source successful CI required")
        jobs = api(f"/repos/{PRIVATE}/actions/runs/{run}/jobs?per_page=100")
        listing = api(f"/repos/{PRIVATE}/actions/runs/{run}/artifacts?per_page=100")
        wanted = {spec[2] for spec in EDITIONS.values() if spec[0] == platform}
        need(listing.get("total_count") == len(wanted) and {row["name"] for row in listing["artifacts"]} == wanted, "Exact CI artifact roster")
        for edition, spec in EDITIONS.items():
            if spec[0] != platform:
                continue
            job = [row for row in jobs["jobs"] if row["name"] == spec[1]]
            need(len(job) == 1 and job[0]["status"] == "completed" and job[0]["conclusion"] == "success", "Exact native job must pass")
            artifact = next(row for row in listing["artifacts"] if row["name"] == spec[2])
            need(artifact.get("expired") is False and artifact.get("workflow_run", {}).get("id") == int(run)
                 and artifact.get("workflow_run", {}).get("head_sha") == source, "Artifact provenance")
            selected[edition] = artifact
    need(sum(row["size_in_bytes"] for row in selected.values()) <= MAX_TOTAL, "Combined artifact size bound")
    modules, assets = pinned_source(source)
    receipt_dir = Path("native-promotion-receipt")
    receipt_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="installer-promotion-") as temporary:
        folder = Path(temporary)
        def worker(edition):
            return prepare(edition, selected[edition], folder, modules, assets, source, runs[EDITIONS[edition][0]])
        with ThreadPoolExecutor(max_workers=4) as pool:
            rows = [row for group in pool.map(worker, EDITIONS) for row in group]
        notes_name = "RELEASE_NOTES_" + VERSION + ".md"
        (folder / notes_name).write_bytes(source_blob("docs/" + notes_name, source))
        rows.append(dict(name=notes_name, size=(folder / notes_name).stat().st_size, sha256=digest(folder / notes_name)))
        need(len(rows) == 17 and len({row["name"] for row in rows}) == 17, "Exact native/proof/notes count")
        checksum_name = "SHA256SUMS-" + VERSION + ".txt"
        (folder / checksum_name).write_text("".join(row["sha256"] + "  " + row["name"] + "\n" for row in sorted(rows, key=lambda row: row["name"])), encoding="ascii", newline="\n")
        rows.append(dict(name=checksum_name, size=(folder / checksum_name).stat().st_size, sha256=digest(folder / checksum_name)))
        wanted = {row["name"]: row for row in rows}
        remote = {row["name"]: row for row in release().get("assets", [])}
        need(set(remote) <= set(wanted), "Unexpected draft asset")
        for name, row in remote.items():
            need(row.get("state") == "uploaded" and row.get("size") == wanted[name]["size"]
                 and row.get("digest") == "sha256:" + wanted[name]["sha256"], "Different draft asset; overwrite refused")
        pending = [str(folder / name) for name in sorted(wanted) if name not in remote]
        if pending:
            result = subprocess.run(["gh", "release", "upload", TAG, *pending, "--repo", PUBLIC], capture_output=True, text=True, timeout=1800)
            need(result.returncode == 0, "Release upload failed; inspect draft before retry")
        remote = {row["name"]: row for row in release().get("assets", [])}
        need(len(remote) == 18 and set(remote) == set(wanted), "Final exact draft asset count")
        for name, row in remote.items():
            need(row.get("state") == "uploaded" and row.get("size") == wanted[name]["size"]
                 and row.get("digest") == "sha256:" + wanted[name]["sha256"], "Uploaded server size/SHA256 mismatch")
            wanted[name]["releaseAssetId"] = row["id"]
        native_checks = {}
        for edition in EDITIONS:
            proof_name = PREFIX + edition + "-bundle-proof.json"
            shutil.copyfile(folder / proof_name, receipt_dir / proof_name)
            native_checks[edition] = dict(archiveIntegrityVerified=True, executableHashMatchesNativeProof=True,
                                         nativeFormat="PE32+-AMD64" if edition.startswith("windows") else "ELF64" if edition.startswith("linux") else "Mach-O64",
                                         nativeMachine="arm64" if edition == "macos-arm64" else "x86_64")
            if edition.startswith("macos"):
                native_checks[edition]["nativeDmgVerificationPassedInWorkflow"] = True
        receipt = dict(status="complete-unpublished-draft", sourceCommit=source, sourceRepository=PRIVATE,
                       releaseId=int(release_id), tag=TAG, workflowCommit=checkout, runs=runs, nativeEditions=list(EDITIONS),
                       modulesVerified=len(modules), assetsVerified=len(assets), sourceModuleHashes=modules, sourceAssetHashes=assets,
                       nativeChecks=native_checks,
                       sourceArtifacts=[dict(edition=edition, id=artifact["id"], name=artifact["name"], size=artifact["size_in_bytes"], sha256=artifact["digest"][7:],
                                             workflowRun=runs[EDITIONS[edition][0]]) for edition, artifact in selected.items()],
                       assets=list(wanted.values()), serverSizesAndDigestsVerified=True, artifactCodeExecuted=False,
                       releasePublished=False, feedChanged=False, overwriteAllowed=False)
        (receipt_dir / "promotion.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        print(json.dumps(dict(status=receipt["status"], assets=18, editions=6, sourceCommit=source)))


if __name__ == "__main__":
    try:
        main()
    except PromotionError as error:
        raise SystemExit(str(error)) from None
    except Exception:
        # Network exceptions can contain short-lived URLs. Never log their text.
        raise SystemExit("Promotion failed; inspect fixed metadata and retained draft assets before retry.") from None
