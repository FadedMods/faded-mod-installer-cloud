#!/usr/bin/env python3
"""Publish only exact artifacts from Outback Steakhouse's public Nexus pack.

Run from a full cloud-repository checkout. Older pinned artifacts are resolved
from catalog Git history, never replaced with a newer Main version.
"""
from __future__ import annotations

import copy
import json
import os
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path

from validate_manifests import (
    DUPLICATE_MOD_INFO_SHA256S, NONPORTABLE_ARCHIVE_SHA256S,
    QUARANTINED_SHA256,
)

ROOT = Path(__file__).resolve().parents[1]
WORLD_ID = "78c689b5-d7a0-49e7-9c2f-b50753098c48"
PACK_URL = f"https://network.fadedmods.com/api/v1/worlds/{WORLD_ID}/pack"
OUTPUT = ROOT / "manifests" / "outback-steakhouse.json"
BAD_HASHES = NONPORTABLE_ARCHIVE_SHA256S | DUPLICATE_MOD_INFO_SHA256S | {QUARANTINED_SHA256}


def fetch_pack():
    request = urllib.request.Request(PACK_URL, headers={"User-Agent": "FadedInstaller-CatalogSync/0.3.4"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read(8 * 1024 * 1024 + 1)
    if len(body) > 8 * 1024 * 1024:
        raise ValueError("Nexus pack exceeds the response limit")
    pack = json.loads(body)
    validate_pack(pack)
    return pack


def validate_pack(pack):
    if pack.get("worldId") != WORLD_ID or pack.get("status") != "published":
        raise ValueError("Expected Outback Steakhouse's published Nexus pack")
    for field in ("packId", "version", "targetPzBuild", "requiredJavaLoaderVersion"):
        if not isinstance(pack.get(field), str) or not pack[field].strip():
            raise ValueError(f"Missing Nexus {field}")
    if not re.fullmatch(r"[a-f0-9]{64}", pack.get("completePackHash", "")):
        raise ValueError("Invalid complete pack hash")
    entries = pack.get("entries")
    if not isinstance(entries, list) or not entries or len(entries) > 10000:
        raise ValueError("Expected a nonempty Nexus mod list")
    seen_ids, seen_server_ids, orders = set(), set(), set()
    for entry in entries:
        for field in ("manifestModId", "serverModId", "version"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValueError(f"Missing pack entry {field}")
        mod_id, server_id, order = entry["manifestModId"], entry["serverModId"], entry.get("loadOrder")
        if mod_id in seen_ids or server_id in seen_server_ids or order in orders:
            raise ValueError("Duplicate Nexus mod identity or load order")
        if type(order) is not int or order < 0:
            raise ValueError("Invalid Nexus load order")
        seen_ids.add(mod_id)
        seen_server_ids.add(server_id)
        orders.add(order)
        if entry.get("kind") not in {"required", "optional"}:
            raise ValueError("Unknown Nexus entry kind")
        hashes = entry.get("artifactHashes")
        if not isinstance(hashes, list) or not hashes or any(
            not isinstance(h, str) or not re.fullmatch(r"[a-f0-9]{64}", h) for h in hashes
        ):
            raise ValueError(f"Missing verified artifact hashes for {mod_id}")
        if BAD_HASHES.intersection(hashes):
            raise ValueError(f"Nexus references quarantined artifacts for {mod_id}")


def matches(entry, mod):
    downloads = mod.get("download_parts") or [mod]
    return (
        mod.get("id") == entry["manifestModId"]
        and mod.get("server_mod_id", mod.get("id")) == entry["serverModId"]
        and mod.get("version") == entry["version"]
        and [d.get("sha256") for d in downloads] == entry["artifactHashes"]
        and all(isinstance(d.get("size_bytes"), int) and d["size_bytes"] > 0 for d in downloads)
        and sum(d["size_bytes"] for d in downloads) == entry.get("downloadSizeBytes")
        and all(str(d.get("download_url", "")).startswith("https://") for d in downloads)
    )


def resolve_catalog(pack, catalogs):
    validate_pack(pack)
    entries = sorted(pack["entries"], key=lambda item: item["loadOrder"])
    found = {}
    loader_fields = None
    for catalog in catalogs:
        for mod in catalog.get("mods", []):
            for entry in entries:
                if entry["manifestModId"] not in found and matches(entry, mod):
                    found[entry["manifestModId"]] = copy.deepcopy(mod)
        loader = catalog.get("java_loader_v3") or {}
        if loader_fields is None and loader.get("version") == pack["requiredJavaLoaderVersion"]:
            loader_fields = {k: copy.deepcopy(v) for k, v in catalog.items() if k.startswith("java_loader")}
        if len(found) == len(entries) and loader_fields is not None:
            break
    missing = [e["manifestModId"] for e in entries if e["manifestModId"] not in found]
    if missing or loader_fields is None:
        raise ValueError(f"Cannot resolve exact Nexus artifacts: {missing}; loader resolved: {loader_fields is not None}")
    return {
        "manifest_version": 1,
        "app_name": "Outback Steakhouse",
        "nexus": {
            "world_id": WORLD_ID, "pack_url": PACK_URL,
            "pack_id": pack["packId"], "version": pack["version"],
            "complete_pack_hash": pack["completePackHash"],
            "target_pz_build": pack["targetPzBuild"],
            "required_java_loader_version": pack["requiredJavaLoaderVersion"],
            "published_at": pack.get("publishedAt"),
            "optional_mod_ids": [e["manifestModId"] for e in entries if e["kind"] == "optional"],
        },
        **loader_fields,
        "mods": [found[e["manifestModId"]] for e in entries],
    }


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, encoding="utf-8")


def catalog_history():
    yield json.loads((ROOT / "manifest.json").read_text(encoding="utf-8-sig"))
    if OUTPUT.exists():
        yield json.loads(OUTPUT.read_text(encoding="utf-8-sig"))
    for commit in git("log", "--format=%H", "--", "manifest.json").splitlines():
        yield json.loads(git("show", f"{commit}:manifest.json"))


def main():
    pack = fetch_pack()
    catalog = resolve_catalog(pack, catalog_history())
    latest = fetch_pack()
    if (latest["packId"], latest["completePackHash"]) != (pack["packId"], pack["completePackHash"]):
        raise ValueError("Nexus pack changed during resolution; retry the synchronization")
    payload = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists() and OUTPUT.read_text(encoding="utf-8") == payload:
        print(f"Outback is current: {pack['version']}, {len(catalog['mods'])} mods")
        return
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=OUTPUT.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
        os.replace(temporary, OUTPUT)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    print(f"Updated Outback: {pack['version']}, {len(catalog['mods'])} exact Nexus entries")


if __name__ == "__main__":
    main()
