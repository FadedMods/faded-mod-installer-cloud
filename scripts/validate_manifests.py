#!/usr/bin/env python3
"""Validate shared manifest metadata and quarantine known unsafe releases."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATHS = (
    PROJECT_ROOT / "manifest.json",
    PROJECT_ROOT / "manifests" / "faded-realms.json",
)
PFC_ID = "ProjectFadedCar"
QUARANTINED_VERSION = "2.1.0"
QUARANTINED_SHA256 = "07927e0a8a470699a5b593516128e52294680f7e87093c2f6920317307fba631"
QUARANTINED_URL = (
    "https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/"
    "mod-assets-2026-08-26-project-faded-car-2.1.0/ProjectFadedCar-v2.1.0.zip"
)
QUARANTINED_ZIP_NAME = "ProjectFadedCar-v2.1.0.zip"


def _download_entries(mod: dict[str, Any]) -> Iterable[dict[str, Any]]:
    yield mod
    parts = mod.get("download_parts")
    if isinstance(parts, list):
        yield from (part for part in parts if isinstance(part, dict))


def validate_manifests(paths: Iterable[Path]) -> list[str]:
    paths = tuple(paths)
    errors: list[str] = []
    pfc_entries: list[tuple[Path, dict[str, Any]]] = []

    for path in paths:
        try:
            document = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot load manifest: {exc}")
            continue

        mods = document.get("mods") if isinstance(document, dict) else None
        if not isinstance(mods, list):
            errors.append(f"{path}: root mods must be a list")
            continue

        matches = [mod for mod in mods if isinstance(mod, dict) and mod.get("id") == PFC_ID]
        if len(matches) != 1:
            errors.append(f"{path}: expected exactly one {PFC_ID} entry, found {len(matches)}")
            continue

        mod = matches[0]
        pfc_entries.append((path, mod))
        if str(mod.get("version", "")) == QUARANTINED_VERSION:
            errors.append(f"{path}: {PFC_ID} version {QUARANTINED_VERSION} is quarantined")

        for download in _download_entries(mod):
            sha256 = str(download.get("sha256", "")).casefold()
            url = str(download.get("download_url", ""))
            zip_name = str(download.get("zip_name", ""))
            if sha256 == QUARANTINED_SHA256:
                errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 SHA-256 is present")
            if url == QUARANTINED_URL:
                errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 URL is present")
            if zip_name.casefold() == QUARANTINED_ZIP_NAME.casefold():
                errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 ZIP name is present")

    if len(pfc_entries) == len(paths) and pfc_entries:
        canonical_path, canonical_entry = pfc_entries[0]
        for path, entry in pfc_entries[1:]:
            if entry != canonical_entry:
                errors.append(
                    f"{path}: {PFC_ID} metadata differs from {canonical_path}; "
                    "Main and Faded Realms must be updated together"
                )

    return errors


def main() -> int:
    errors = validate_manifests(MANIFEST_PATHS)
    if errors:
        print(f"Manifest safety validation FAILED ({len(errors)} issue(s)):")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Manifest safety validation passed; ProjectFadedCar metadata is synchronized and 2.1.0 is quarantined.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
