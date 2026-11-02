"""Validate Stardew's separate SMAPI catalog and optional local release archives.

This validator reads metadata and ZIP bytes only; it never loads mod assemblies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import urlsplit
import zipfile


MAX_JSON = 256 * 1024
MAX_DOWNLOAD = 384 * 1024 * 1024
MAX_UNPACKED = 768 * 1024 * 1024
MAX_FILES = 8192
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
FOLDER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,95}")
RELEASE_PATH = re.compile(r"/FadedMods/faded-mod-installer-cloud/releases/download/[A-Za-z0-9._-]+/[A-Za-z0-9._-]+\.zip")
RESERVED = {"con", "prn", "aux", "nul", *{f"com{i}" for i in range(1, 10)}, *{f"lpt{i}" for i in range(1, 10)}}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def unique_pairs(rows):
    result = {}
    for key, value in rows:
        check(key not in result, "Duplicate JSON property: " + key)
        result[key] = value
    return result


def json_document(raw):
    check(0 < len(raw) <= MAX_JSON, "JSON byte bound")
    value = json.loads(raw, object_pairs_hook=unique_pairs,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError("Nonfinite JSON")))
    check(type(value) is dict, "JSON object required")
    return value


def version(value):
    check(type(value) is str and re.fullmatch(r"\d{1,6}\.\d{1,6}\.\d{1,6}", value), "Component version")
    return tuple(map(int, value.split(".")))


def safe_folder(value):
    return (type(value) is str and FOLDER.fullmatch(value) and not value.endswith(".")
            and value.partition(".")[0].casefold() not in RESERVED)


def validate_object(value):
    check(type(value) is dict and type(value.get("schema")) is int and value["schema"] == 1
          and value.get("product") == "stardew-valley" and value.get("channel") == "production", "Product/schema/channel")
    check(version(value.get("minimumInstallerVersion")) >= (0, 3, 24), "Stardew installer version floor")
    check(type(value.get("runtime")) is dict and type(value.get("mods")) is list and len(value["mods"]) <= 128, "Component groups")
    check(value["runtime"].get("id") == "StardewModFramework.Runtime", "Framework identity")
    entries = [value["runtime"], *value["mods"]]
    ids, folders = {}, set()
    for index, row in enumerate(entries):
        check(type(row) is dict, "Component object")
        identity = row.get("id")
        check(type(identity) is str and ID.fullmatch(identity), "SMAPI component identity")
        check(identity.casefold() not in ids and row.get("kind") == ("framework" if index == 0 else "mod"), "Unique component identity/kind")
        folder = row.get("folder")
        check(safe_folder(folder) and folder.casefold() not in folders, "Unique safe mod folder")
        folders.add(folder.casefold())
        check(type(row.get("entryDll")) is str and FOLDER.fullmatch(row["entryDll"])
              and row["entryDll"].endswith(".dll"), "Entry DLL basename")
        for field, maximum in (("name", 128), ("description", 4096)):
            check(type(row.get(field)) is str and 0 < len(row[field]) <= maximum
                  and not any(ord(char) < 32 for char in row[field]), "Bounded display metadata")
        version(row.get("version"))
        version(row.get("minimumApiVersion"))
        version(row.get("minimumGameVersion"))
        check(type(row.get("size")) is int and 0 < row["size"] <= MAX_DOWNLOAD, "Component download size")
        check(type(row.get("sha256")) is str and re.fullmatch(r"[a-f0-9]{64}", row["sha256"]), "Component SHA256")
        check(type(row.get("url")) is str and len(row["url"]) <= 2048, "Component URL")
        url = urlsplit(row["url"])
        check(url.scheme == "https" and url.hostname == "github.com" and url.port in (None, 443)
              and not any((url.username, url.password, url.query, url.fragment))
              and RELEASE_PATH.fullmatch(url.path), "Immutable official HTTPS release URL")
        check(type(row.get("dependencies")) is list and len(row["dependencies"]) <= 128, "Dependency list")
        ids[identity.casefold()] = row
    graph = {}
    for row in entries:
        dependencies = set()
        for dependency in row["dependencies"]:
            check(type(dependency) is dict and set(dependency) == {"id", "minimumVersion"}, "Dependency object")
            identity = dependency["id"]
            check(type(identity) is str and identity.casefold() in ids, "Dependency present in catalog")
            target = ids[identity.casefold()]
            check(identity == target["id"] and identity.casefold() not in dependencies
                  and identity != row["id"], "Unique nonself dependency identity")
            check(version(target["version"]) >= version(dependency["minimumVersion"]), "Dependency version satisfied")
            dependencies.add(identity.casefold())
        graph[row["id"].casefold()] = dependencies
    active, complete = set(), set()

    def visit(identity):
        check(identity not in active, "Dependency cycle")
        if identity in complete:
            return
        active.add(identity)
        for dependency in graph[identity]:
            visit(dependency)
        active.remove(identity)
        complete.add(identity)

    for identity in graph:
        visit(identity)
    return len(entries)


def validate_archive(row, path):
    check(path.stat().st_size == row["size"], "Archive size: " + path.name)
    check(hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], "Archive SHA256: " + path.name)
    records = {}
    with zipfile.ZipFile(path) as archive:
        check(len(archive.infolist()) <= MAX_FILES, "Archive member bound")
        check(sum(info.file_size for info in archive.infolist()) <= MAX_UNPACKED, "Archive expanded byte bound")
        names = set()
        for info in archive.infolist():
            check(info.orig_filename == info.filename, "Archive mod folder boundary: noncanonical filename")
            path_parts = PurePosixPath(info.filename).parts
            raw_parts = info.filename.rstrip("/").split("/")
            check(path_parts and path_parts[0] == row["folder"] and not info.filename.startswith("/")
                  and not any(part in {"", ".", ".."} for part in raw_parts)
                  and not any(char in info.filename for char in ("\\", ":", "\x00")), "Archive mod folder boundary")
            check(not stat.S_ISLNK(info.external_attr >> 16) and not info.flag_bits & 1, "Archive plain unencrypted files")
            check(info.filename.casefold() not in names, "Archive duplicate/case-colliding member")
            names.add(info.filename.casefold())
            if not info.is_dir():
                data = archive.read(info)
                records[info.filename] = {"size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        prefix = row["folder"] + "/"
        check(prefix + row["entryDll"] in records and prefix + "manifest.json" in records, "Archive entry DLL and manifest")
        manifest = json_document(archive.read(prefix + "manifest.json"))
        for field, key in (("UniqueID", "id"), ("Version", "version"), ("EntryDll", "entryDll"), ("MinimumApiVersion", "minimumApiVersion")):
            check(manifest.get(field) == row[key], "Archive manifest agreement: " + field)
        if "MinimumGameVersion" in manifest:
            check(version(row["minimumGameVersion"]) >= version(manifest["MinimumGameVersion"]), "Archive minimum game version")
        required = {item["UniqueID"]: item.get("MinimumVersion", "0.0.0")
                    for item in manifest.get("Dependencies", []) if item.get("IsRequired", True)}
        listed = {item["id"]: item["minimumVersion"] for item in row["dependencies"]}
        check(required == listed, "Archive required dependency agreement")
    return records


def validate(path, archive_dir=None):
    value = json_document(path.read_bytes())
    count = validate_object(value)
    if archive_dir is not None:
        for row in [value["runtime"], *value["mods"]]:
            validate_archive(row, archive_dir / PurePosixPath(urlsplit(row["url"]).path).name)
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path, nargs="?", default=Path("stardew-valley-manifest.json"))
    parser.add_argument("--archive-dir", type=Path)
    arguments = parser.parse_args()
    print(f"Stardew Valley catalog valid: {validate(arguments.catalog, arguments.archive_dir)} separate SMAPI components.")
