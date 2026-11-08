#!/usr/bin/env python3
"""Stage the Common Sense Reborn Test 2.1.4 catalog switch.

Main and Faded Realms publish Test 2.1.4. Without --apply this prints those
entries. With --apply it rewrites only CommonSenseRebornTest and refuses the
published package hash. Production CommonSenseReborn, FJL, Deadflow, and PZ
Optimized stay untouched. requiresJavaLoader stays false and no Java plugin
fields are added.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MOD_ID = "CommonSenseRebornTest"
BASELINE_VERSION = "2.1.4"
VERSION = "2.1.4"
UPDATED_AT = "2026-11-08"
ZIP_NAME = "CommonSenseRebornTest-v2.1.4.zip"
TAG = "mod-assets-2026-11-08-csr-test-2.1.4-b42.22"
DOWNLOAD_URL = (
    "https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/"
    f"{TAG}/{ZIP_NAME}"
)
DESCRIPTION = (
    "CSR Test 2.1.4 preserves native PZ version and integrity reporting, "
    "including old saved preferences, and admits reviewed pre-release revision "
    "3d39148846. FJL remains optional. Never enable with Main."
)
CURRENT_SHA256 = "10ef8f347b716e4c9fa660d3dad2ee6d09527daa120262b350028ab5db5b4eb2"
REQUIRED_PUBLICATION_FIELDS = (
    "download_url",
    "sha256",
    "size_bytes",
    "uncompressed_size_bytes",
    "required_free_bytes",
)
PRESERVED_FIELDS = (
    "id",
    "server_mod_id",
    "name",
    "requiresJavaLoader",
)


class CatalogError(RuntimeError):
    pass


def load_document(path: Path) -> tuple[dict, str]:
    raw = path.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    document = json.loads(text)
    if not isinstance(document, dict) or not isinstance(document.get("mods"), list):
        raise CatalogError(f"{path} has no mods list")
    return document, newline


def entries(document: dict) -> list[dict]:
    return [mod for mod in document["mods"] if isinstance(mod, dict) and mod.get("id") == MOD_ID]


def require_baseline(path: Path, document: dict) -> dict:
    matches = entries(document)
    if len(matches) != 1:
        raise CatalogError(f"{path} has {len(matches)} {MOD_ID} entries")
    current = matches[0]
    if current.get("version") != BASELINE_VERSION:
        raise CatalogError(f"{path} {MOD_ID} baseline is not {BASELINE_VERSION}")
    if current.get("sha256") != CURRENT_SHA256:
        raise CatalogError(f"{path} {MOD_ID} package hash is not the published {BASELINE_VERSION} package")
    if current.get("requiresJavaLoader") is not False:
        raise CatalogError(f"{path} {MOD_ID} must keep requiresJavaLoader false")
    return current


def read_publication(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CatalogError(f"Cannot read publication record {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CatalogError("Publication record must be a JSON object")
    nested = value.get("required_from_uploaded_package")
    if isinstance(nested, dict):
        return nested
    return value


def missing_fields(publication: dict) -> list[str]:
    missing = []
    for field in REQUIRED_PUBLICATION_FIELDS:
        value = publication.get(field)
        if value is None or value == "":
            missing.append(field)
    return missing


def validate_publication(publication: dict) -> dict:
    missing = missing_fields(publication)
    if missing:
        raise CatalogError("Publication record is missing " + ", ".join(missing))
    url = str(publication["download_url"])
    if url != DOWNLOAD_URL:
        raise CatalogError(f"download_url must be {DOWNLOAD_URL}")
    digest = str(publication["sha256"])
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise CatalogError("sha256 must be 64 lowercase hex characters")
    if digest == CURRENT_SHA256:
        raise CatalogError(f"sha256 is still the published {BASELINE_VERSION} package")
    numbers = {}
    for field in ("size_bytes", "uncompressed_size_bytes", "required_free_bytes"):
        value = publication[field]
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise CatalogError(f"{field} must be a positive integer")
        numbers[field] = value
    if numbers["required_free_bytes"] < numbers["uncompressed_size_bytes"]:
        raise CatalogError("required_free_bytes is smaller than the uncompressed package")
    return {
        "version": VERSION,
        "description": DESCRIPTION,
        "updated_at": UPDATED_AT,
        "download_url": url,
        "zip_name": ZIP_NAME,
        "size_bytes": numbers["size_bytes"],
        "sha256": digest,
        "uncompressed_size_bytes": numbers["uncompressed_size_bytes"],
        "required_free_bytes": numbers["required_free_bytes"],
    }


def planned_entry(current: dict, changes: dict) -> dict:
    updated = dict(current)
    for field in PRESERVED_FIELDS:
        if field not in current:
            raise CatalogError(f"{MOD_ID} entry is missing preserved field {field}")
    unknown = [field for field in changes if field not in current]
    if unknown:
        raise CatalogError("Refusing to add catalog fields " + ", ".join(unknown))
    updated.update(changes)
    for field in PRESERVED_FIELDS:
        if updated[field] != current[field]:
            raise CatalogError(f"Preserved {MOD_ID} field changed: {field}")
    return updated


def object_span(text: str, start: int) -> tuple[int, int]:
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        character = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return start, index + 1
    raise CatalogError(f"{MOD_ID} object is not closed")


def entry_span(text: str) -> tuple[int, int]:
    marker = '\n    {\n      "id": "CommonSenseRebornTest",\n'
    start = text.find(marker)
    if start < 0 or text.find(marker, start + 1) >= 0:
        raise CatalogError("CommonSenseRebornTest object marker is missing or ambiguous")
    return object_span(text, start + 1)


def render_entry(entry: dict) -> str:
    rendered = json.dumps(entry, indent=2, ensure_ascii=False)
    return "\n".join("    " + line for line in rendered.splitlines())


def apply_to_text(text: str, entry: dict) -> str:
    start, end = entry_span(text)
    current = json.loads(text[start:end])
    if current.get("id") != MOD_ID:
        raise CatalogError("Located object is not CommonSenseRebornTest")
    replacement = render_entry(entry)
    if json.loads(replacement) != entry:
        raise CatalogError("Rendered object does not round-trip")
    updated = text[:start] + replacement + text[end:]
    document = json.loads(updated)
    matches = entries(document)
    if len(matches) != 1 or matches[0] != entry:
        raise CatalogError("Updated catalog does not contain the planned entry")
    return updated


def outside_entry(document: dict) -> tuple:
    mods = [mod for mod in document["mods"] if not (isinstance(mod, dict) and mod.get("id") == MOD_ID)]
    metadata = {key: value for key, value in document.items() if key != "mods"}
    order = [mod.get("id") if isinstance(mod, dict) else None for mod in document["mods"]]
    return metadata, mods, order


def stage_catalog(path: Path, changes: dict, apply: bool) -> dict:
    raw = path.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    document = json.loads(text)
    current = require_baseline(path, document)
    entry = planned_entry(current, changes)
    updated = apply_to_text(text, entry)
    if apply:
        path.write_bytes(updated.replace("\n", newline).encode("utf-8"))
        written, _ = load_document(path)
        if entries(written)[0] != entry:
            raise CatalogError(f"{path} did not retain the planned entry")
        if outside_entry(written) != outside_entry(document):
            raise CatalogError(f"{path} changed something other than {MOD_ID}")
    return {"path": str(path), "current": current, "planned": entry, "applied": apply}


def report(root: Path, publication_path: Path | None, apply: bool) -> dict:
    catalogs = [root / "manifest.json", root / "manifests" / "faded-realms.json"]
    currents = []
    for path in catalogs:
        document, _ = load_document(path)
        currents.append(require_baseline(path, document))
    if currents[0] != currents[1]:
        raise CatalogError("Main and Faded Realms CommonSenseRebornTest entries differ")
    publication = read_publication(publication_path) if publication_path else {}
    missing = missing_fields(publication)
    result = {
        "catalogs": [str(path) for path in catalogs],
        "baseline_version": BASELINE_VERSION,
        "current": currents[0],
        "entries_identical": True,
        "required_publication_fields": list(REQUIRED_PUBLICATION_FIELDS),
        "missing_publication_fields": missing,
        "expected_download_url": DOWNLOAD_URL,
        "applied": False,
    }
    if apply:
        if publication_path is None:
            raise CatalogError("Applying the catalog switch requires --publication")
        changes = validate_publication(publication)
        staged = [stage_catalog(path, changes, True) for path in catalogs]
        if staged[0]["planned"] != staged[1]["planned"]:
            raise CatalogError("Planned Main and Faded Realms entries differ")
        result["applied"] = True
        result["planned"] = staged[0]["planned"]
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--publication", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = report(args.root, args.publication, args.apply)
    except CatalogError as exc:
        print(f"CSR Test catalog switch refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.apply and not result["applied"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
