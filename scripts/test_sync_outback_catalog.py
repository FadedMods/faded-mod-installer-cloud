import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import sync_outback_catalog as sync


class OutbackCatalogTests(unittest.TestCase):
    def setUp(self):
        self.mod = {"id": "Example", "server_mod_id": "ExampleServer", "version": "1.0",
                    "name": "Example", "description": "Example mod", "sha256": "a" * 64,
                    "size_bytes": 100, "zip_name": "Example.zip", "download_url": "https://example.com/Example.zip"}
        self.entry = {"manifestModId": "Example", "serverModId": "ExampleServer", "version": "1.0",
                      "loadOrder": 0, "kind": "required", "artifactHashes": ["a" * 64], "downloadSizeBytes": 100}
        self.pack = {"worldId": sync.WORLD_ID, "packId": "pack-one", "version": "pack-1", "status": "published",
                     "targetPzBuild": "42.20.4", "requiredJavaLoaderVersion": "0.4.4",
                     "completePackHash": "c" * 64, "entries": [self.entry]}
        self.catalog = {"mods": [self.mod], "java_loader_v3": {"version": "0.4.4", "artifacts": []}}

    def test_older_exact_pack_wins_over_latest_main(self):
        latest = copy.deepcopy(self.catalog)
        latest["mods"][0].update(version="1.1", sha256="b" * 64)
        result = sync.resolve_catalog(self.pack, [latest, self.catalog])
        self.assertEqual(result["mods"], [self.mod])
        self.assertEqual(result["nexus"]["pack_id"], "pack-one")
        self.assertEqual(result["java_loader_v3"], self.catalog["java_loader_v3"])

    def test_missing_or_wrong_version_hash_identity_size_and_loader_fail_closed(self):
        for field, value in [("version", "2"), ("sha256", "b" * 64), ("server_mod_id", "wrong"), ("size_bytes", 99)]:
            with self.subTest(field=field):
                catalog = copy.deepcopy(self.catalog)
                catalog["mods"][0][field] = value
                with self.assertRaisesRegex(ValueError, "Cannot resolve exact"):
                    sync.resolve_catalog(self.pack, [catalog])
        with self.assertRaises(ValueError):
            sync.resolve_catalog(self.pack, [{"mods": [self.mod]}])

    def test_multipart_hash_order_and_load_order_are_preserved(self):
        second_mod = {**self.mod, "id": "Second", "server_mod_id": "Second",
                      "download_parts": [
                          {"sha256": "b" * 64, "size_bytes": 10, "download_url": "https://example.com/1.zip"},
                          {"sha256": "d" * 64, "size_bytes": 20, "download_url": "https://example.com/2.zip"}]}
        second_entry = {**self.entry, "manifestModId": "Second", "serverModId": "Second", "loadOrder": 1,
                        "kind": "optional", "artifactHashes": ["b" * 64, "d" * 64], "downloadSizeBytes": 30}
        self.pack["entries"] = [second_entry, self.entry]
        self.catalog["mods"] = [second_mod, self.mod]
        result = sync.resolve_catalog(self.pack, [self.catalog])
        self.assertEqual([m["id"] for m in result["mods"]], ["Example", "Second"])
        self.assertEqual(result["nexus"]["optional_mod_ids"], ["Second"])
        second_entry["artifactHashes"].reverse()
        with self.assertRaises(ValueError):
            sync.resolve_catalog(self.pack, [self.catalog])

    def test_duplicate_empty_foreign_unpublished_and_quarantined_packs_are_rejected(self):
        for key, value in [("entries", []), ("entries", [self.entry, self.entry]), ("worldId", "other"), ("status", "draft")]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                sync.resolve_catalog({**self.pack, key: value}, [self.catalog])
        self.entry["artifactHashes"] = [sync.QUARANTINED_SHA256]
        with self.assertRaisesRegex(ValueError, "quarantined"):
            sync.resolve_catalog(self.pack, [self.catalog])

    def test_failed_resolution_or_mid_refresh_change_never_overwrites_catalog(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "catalog.json"
            output.write_text("previous valid catalog")
            with patch.object(sync, "OUTPUT", output), patch.object(sync, "fetch_pack", return_value=self.pack), patch.object(
                sync, "catalog_history", return_value=iter([])
            ), self.assertRaises(ValueError):
                sync.main()
            self.assertEqual(output.read_text(), "previous valid catalog")
            with patch.object(sync, "OUTPUT", output), patch.object(
                sync, "fetch_pack", side_effect=[self.pack, {**self.pack, "packId": "changed"}]
            ), patch.object(sync, "catalog_history", return_value=iter([self.catalog])), self.assertRaises(ValueError):
                sync.main()
            self.assertEqual(output.read_text(), "previous valid catalog")

    def test_successful_sync_is_idempotent_and_writes_only_output(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "catalog.json"
            with patch.object(sync, "OUTPUT", output), patch.object(sync, "fetch_pack", return_value=self.pack), patch.object(
                sync, "catalog_history", side_effect=lambda: iter([self.catalog])
            ):
                sync.main()
                first = output.stat().st_mtime_ns
                sync.main()
                self.assertEqual(output.stat().st_mtime_ns, first)
            self.assertEqual(json.loads(output.read_text())["mods"], [self.mod])
            self.assertEqual(list(Path(directory).iterdir()), [output])


if __name__ == "__main__":
    unittest.main()
