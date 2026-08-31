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
SYNCHRONIZED_RELEASE_IDS = (
    "MassiveKI5Pack",
    "NeverSurviveAlone",
    "BuckShotRoulette",
    "FadedJavaLoaderBridge",
    "FadedNexus",
    "ISyncYouSyncWeAllSyncForDeSync",
)
SHARED_RELEASE_FIELDS = (
    "version",
    "description",
    "updated_at",
    "download_url",
    "download_parts",
    "zip_name",
    "size_bytes",
    "sha256",
    "uncompressed_size_bytes",
    "required_free_bytes",
)
QUARANTINED_VERSION = "2.1.0"
QUARANTINED_SHA256 = "07927e0a8a470699a5b593516128e52294680f7e87093c2f6920317307fba631"
QUARANTINED_URL = (
    "https://github.com/FadedMods/faded-mod-installer-cloud/releases/download/"
    "mod-assets-2026-08-26-project-faded-car-2.1.0/ProjectFadedCar-v2.1.0.zip"
)
QUARANTINED_ZIP_NAME = "ProjectFadedCar-v2.1.0.zip"
NONPORTABLE_ARCHIVE_SHA256S = frozenset(
    {
        # Windows ZipArchive wrote backslashes into both ZIP filename indexes.
        "626333c10c4f4e0ae5b85805f610e746394bee213472adb33bced23bb5234361",
        "db1fe13f17d8ec2cc445b0976b90198235287f98e6d15b733dc504900170a3a8",
        "1cc23f0558909f31d6cd68bf4eef167defc35661568205daacf2daea0a07e922",
        "060acbccc8f57dcd19a22bb57ff997930cf3fcd76c919d4f8f1b000a71a52729",
    }
)
JAVA_PLUGIN_FIELDS = (
    "minimumJavaLoaderVersion",
    "javaEnvironment",
    "javaPluginId",
    "javaPluginVersion",
    "javaPluginMode",
)


def _download_entries(mod: dict[str, Any]) -> Iterable[dict[str, Any]]:
    yield mod
    parts = mod.get("download_parts")
    if isinstance(parts, list):
        yield from (part for part in parts if isinstance(part, dict))


def validate_manifests(paths: Iterable[Path]) -> list[str]:
    paths = tuple(paths)
    errors: list[str] = []
    pfc_entries: list[tuple[Path, dict[str, Any]]] = []
    synchronized_entries: dict[str, list[tuple[Path, dict[str, Any]]]] = {
        mod_id: [] for mod_id in SYNCHRONIZED_RELEASE_IDS
    }

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

        for mod in (entry for entry in mods if isinstance(entry, dict)):
            populated_java_fields = [
                field
                for field in JAVA_PLUGIN_FIELDS
                if str(mod.get(field) or "").strip()
            ]
            if populated_java_fields and mod.get("requiresJavaLoader") is not True:
                errors.append(
                    f"{path}: {mod.get('id') or '<missing id>'} includes "
                    f"{', '.join(populated_java_fields)} but requiresJavaLoader is not true; "
                    "legacy installer clients reject the entire catalog"
                )

            for download in _download_entries(mod):
                sha256 = str(download.get("sha256", "")).casefold()
                if sha256 in NONPORTABLE_ARCHIVE_SHA256S:
                    errors.append(
                        f"{path}: {mod.get('id') or '<missing id>'} references a quarantined "
                        "Windows-path ZIP that cannot be extracted normally on Linux"
                    )

        pfc_matches = [mod for mod in mods if isinstance(mod, dict) and mod.get("id") == PFC_ID]
        if len(pfc_matches) != 1:
            errors.append(f"{path}: expected exactly one {PFC_ID} entry, found {len(pfc_matches)}")
        else:
            pfc_mod = pfc_matches[0]
            pfc_entries.append((path, pfc_mod))
            if str(pfc_mod.get("version", "")) == QUARANTINED_VERSION:
                errors.append(f"{path}: {PFC_ID} version {QUARANTINED_VERSION} is quarantined")

            for download in _download_entries(pfc_mod):
                sha256 = str(download.get("sha256", "")).casefold()
                url = str(download.get("download_url", ""))
                zip_name = str(download.get("zip_name", ""))
                if sha256 == QUARANTINED_SHA256:
                    errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 SHA-256 is present")
                if url == QUARANTINED_URL:
                    errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 URL is present")
                if zip_name.casefold() == QUARANTINED_ZIP_NAME.casefold():
                    errors.append(f"{path}: quarantined {PFC_ID} 2.1.0 ZIP name is present")

        for mod_id in SYNCHRONIZED_RELEASE_IDS:
            matches = [mod for mod in mods if isinstance(mod, dict) and mod.get("id") == mod_id]
            if len(matches) != 1:
                errors.append(f"{path}: expected exactly one {mod_id} entry, found {len(matches)}")
            else:
                synchronized_entries[mod_id].append((path, matches[0]))

    if len(pfc_entries) == len(paths) and pfc_entries:
        canonical_path, canonical_entry = pfc_entries[0]
        for path, entry in pfc_entries[1:]:
            if entry != canonical_entry:
                errors.append(
                    f"{path}: {PFC_ID} metadata differs from {canonical_path}; "
                    "Main and Faded Realms must be updated together"
                )

    for mod_id, entries in synchronized_entries.items():
        if len(entries) != len(paths) or not entries:
            continue
        canonical_path, canonical_entry = entries[0]
        for path, entry in entries[1:]:
            differing_fields = [
                field
                for field in SHARED_RELEASE_FIELDS
                if entry.get(field) != canonical_entry.get(field)
            ]
            if differing_fields:
                errors.append(
                    f"{path}: {mod_id} release metadata differs from {canonical_path} "
                    f"for {', '.join(differing_fields)}; Main and Faded Realms "
                    "must be updated together"
                )

    return errors


def main() -> int:
    errors = validate_manifests(MANIFEST_PATHS)
    if errors:
        print(f"Manifest safety validation FAILED ({len(errors)} issue(s)):")
        for error in errors:
            print(f" - {error}")
        return 1
    print(
        "Manifest safety validation passed; ProjectFadedCar metadata is synchronized "
        "and 2.1.0 is quarantined; known Windows-path ZIPs are quarantined; shared "
        "release metadata is synchronized."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
