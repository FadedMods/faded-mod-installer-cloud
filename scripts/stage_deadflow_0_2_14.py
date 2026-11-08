#!/usr/bin/env python3
"""Stage the Deadflow 0.2.14 catalog switch for Main and Faded Realms.

Main and Faded Realms now publish 0.2.14. Without --apply this prints those
entries. With --apply it rewrites only the two Deadflow objects, and it refuses
the published package hash.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CATALOGS = (ROOT / "manifest.json", ROOT / "manifests" / "faded-realms.json")
MOD_ID = "Deadflow"
BASELINE_VERSION = "0.2.14"
VERSION = "0.2.14"
UPDATED_AT = "2026-11-08"
ZIP_NAME = "Deadflow-v0.2.14.zip"
TAG = "mod-assets-2026-11-08-deadflow-0.2.14-b42.22"
DOWNLOAD_URL = (
    "https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/"
    f"{TAG}/{ZIP_NAME}"
)
DESCRIPTION = (
    "Population authority for new Deadflow worlds on 42.20.4, 42.21 and 42.22 "
    "(Windows and Linux dedicated). Stock 42.22 includes reviewed revisions "
    "e013dbb529 and 3d39148846. PZ Optimized 0.4.0 and 0.4.1 remain limited to "
    "revision e013dbb529. PZ Optimized 0.4.3 is the reviewed full payload for "
    "revision 3d39148846 after offline repair. Older saved zombie snapshot "
    "formats are not migrated. Requires FJL 0.6.7+ and its fixed Bridge."
)
CURRENT_SHA256 = "4ec8a0c18a2a0f7d779301dcc69fb027ea4d116bf5190d18140cd555c2e97d34"
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
    "javaEnvironment",
    "javaPluginId",
    "javaPluginMode",
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


def deadflow_entries(document: dict) -> list[dict]:
    return [mod for mod in document["mods"] if isinstance(mod, dict) and mod.get("id") == MOD_ID]


def require_baseline(path: Path, document: dict) -> dict:
    matches = deadflow_entries(document)
    if len(matches) != 1:
        raise CatalogError(f"{path} has {len(matches)} Deadflow entries")
    current = matches[0]
    if current.get("version") != BASELINE_VERSION or current.get("javaPluginVersion") != BASELINE_VERSION:
        raise CatalogError(f"{path} Deadflow baseline is not {BASELINE_VERSION}")
    if current.get("sha256") != CURRENT_SHA256:
        raise CatalogError(f"{path} Deadflow package hash is not the published {BASELINE_VERSION} package")
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
        "javaPluginVersion": VERSION,
        "minimumJavaLoaderVersion": "0.6.7",
    }


def planned_entry(current: dict, changes: dict) -> dict:
    updated = dict(current)
    for field in PRESERVED_FIELDS:
        if field not in current:
            raise CatalogError(f"Deadflow entry is missing preserved field {field}")
    unknown = [field for field in changes if field not in current]
    if unknown:
        raise CatalogError("Refusing to add catalog fields " + ", ".join(unknown))
    updated.update(changes)
    for field in PRESERVED_FIELDS:
        if updated[field] != current[field]:
            raise CatalogError(f"Preserved Deadflow field changed: {field}")
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
    raise CatalogError("Deadflow object is not closed")


def deadflow_span(text: str) -> tuple[int, int]:
    marker = '\n    {\n      "id": "Deadflow",\n'
    start = text.find(marker)
    if start < 0 or text.find(marker, start + 1) >= 0:
        raise CatalogError("Deadflow object marker is missing or ambiguous")
    return object_span(text, start + 1)


def render_entry(entry: dict) -> str:
    rendered = json.dumps(entry, indent=2, ensure_ascii=False)
    return "\n".join("    " + line for line in rendered.splitlines())


def apply_to_text(text: str, entry: dict) -> str:
    start, end = deadflow_span(text)
    current = json.loads(text[start:end])
    if current.get("id") != MOD_ID:
        raise CatalogError("Located object is not Deadflow")
    replacement = render_entry(entry)
    if json.loads(replacement) != entry:
        raise CatalogError("Rendered Deadflow object does not round-trip")
    updated = text[:start] + replacement + text[end:]
    document = json.loads(updated)
    matches = deadflow_entries(document)
    if len(matches) != 1 or matches[0] != entry:
        raise CatalogError("Updated catalog does not contain the planned Deadflow entry")
    return updated


def outside_deadflow(document: dict) -> tuple:
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
        if deadflow_entries(written)[0] != entry:
            raise CatalogError(f"{path} did not retain the planned Deadflow entry")
        if outside_deadflow(written) != outside_deadflow(document):
            raise CatalogError(f"{path} changed something other than Deadflow")
    return {"path": str(path), "current": current, "planned": entry, "applied": apply}


def report(root: Path, publication_path: Path | None, apply: bool) -> dict:
    catalogs = [root / "manifest.json", root / "manifests" / "faded-realms.json"]
    currents = []
    for path in catalogs:
        document, _ = load_document(path)
        currents.append(require_baseline(path, document))
    if currents[0] != currents[1]:
        raise CatalogError("Main and Faded Realms Deadflow entries differ")
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
        print(f"Deadflow catalog switch refused: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.apply and not result["applied"]:
        return 2
    if args.apply and result["missing_publication_fields"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
