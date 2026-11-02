import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import validate_stardew_catalog as catalog


ROOT = Path(__file__).resolve().parents[1]


class StardewCatalogTests(unittest.TestCase):
    def setUp(self):
        self.value = json.loads((ROOT / "stardew-valley-manifest.json").read_bytes())

    def test_real_catalog_has_framework_and_darkdew_as_separate_components(self):
        self.assertEqual(catalog.validate_object(self.value), 2)
        self.assertEqual(self.value["runtime"]["id"], "StardewModFramework.Runtime")
        self.assertEqual(self.value["mods"][0]["dependencies"], [
            {"id": "StardewModFramework.Runtime", "minimumVersion": "0.2.0"}])

    def test_catalog_contract_and_numeric_types_are_not_coerced(self):
        variants = [dict(schema=True), dict(product="schedule-i"), dict(channel="development"),
                    dict(minimumInstallerVersion="0.3.23"), dict(mods={})]
        for change in variants:
            with self.subTest(change=change), self.assertRaises(ValueError):
                catalog.validate_object(dict(self.value, **change))
        for field, wrong in (("size", True), ("sha256", "x" * 64), ("version", "latest"),
                             ("description", "bad\ncontrol")):
            value = copy.deepcopy(self.value)
            value["runtime"][field] = wrong
            with self.subTest(field=field), self.assertRaises(ValueError):
                catalog.validate_object(value)

    def test_urls_are_immutable_official_release_zips(self):
        url = self.value["runtime"]["url"]
        for wrong in (url.replace("https:", "http:"), url.replace("github.com", "evil.example"),
                      url + "?token=mutable", url + "#fragment", url.replace(".zip", ".fmod"),
                      url.replace("github.com/", "github.com:444/"),
                      url.replace("github.com/", "attacker@github.com/"),
                      url.replace("StardewModFramework-0.2.0.zip", "..%2foutside.zip")):
            value = copy.deepcopy(self.value)
            value["runtime"]["url"] = wrong
            with self.subTest(url=wrong), self.assertRaises(ValueError):
                catalog.validate_object(value)

    def test_mod_folders_are_portable_and_unique(self):
        for folder in ("../outside", "C:\\outside", "CON", "aux.txt", "bad.", "bad "):
            value = copy.deepcopy(self.value)
            value["mods"][0]["folder"] = folder
            with self.subTest(folder=folder), self.assertRaises(ValueError):
                catalog.validate_object(value)
        value = copy.deepcopy(self.value)
        value["mods"][0]["folder"] = value["runtime"]["folder"].lower()
        with self.assertRaisesRegex(ValueError, "folder"):
            catalog.validate_object(value)

    def test_identity_collisions_and_entry_paths_are_refused(self):
        value = copy.deepcopy(self.value)
        value["mods"][0]["id"] = value["runtime"]["id"].lower()
        with self.assertRaisesRegex(ValueError, "identity"):
            catalog.validate_object(value)
        for name in ("../Mod.dll", "sub/Mod.dll", "Mod.exe"):
            value = copy.deepcopy(self.value)
            value["mods"][0]["entryDll"] = name
            with self.subTest(name=name), self.assertRaises(ValueError):
                catalog.validate_object(value)

    def test_dependency_must_exist_have_enough_version_and_be_unique(self):
        for dependency in ({"id": "missing.mod", "minimumVersion": "0.1.0"},
                           {"id": "StardewModFramework.Runtime", "minimumVersion": "9.0.0"},
                           {"id": "Darkdew.Valley", "minimumVersion": "0.1.0"}):
            value = copy.deepcopy(self.value)
            value["mods"][0]["dependencies"] = [dependency]
            with self.subTest(dependency=dependency), self.assertRaises(ValueError):
                catalog.validate_object(value)
        value = copy.deepcopy(self.value)
        value["mods"][0]["dependencies"] *= 2
        with self.assertRaises(ValueError):
            catalog.validate_object(value)

    def test_dependency_cycles_are_refused(self):
        self.value["runtime"]["dependencies"] = [{"id": "Darkdew.Valley", "minimumVersion": "0.1.1"}]
        with self.assertRaisesRegex(ValueError, "cycle"):
            catalog.validate_object(self.value)

    def test_json_duplicate_properties_nonfinite_and_bounds_are_refused(self):
        for raw in (b'{"schema": 1,"schema": 2}', b'{"value": NaN}', b'[]',
                    b' ' * (catalog.MAX_JSON + 1)):
            with self.subTest(raw=raw[:40]), self.assertRaises(ValueError):
                catalog.json_document(raw)

    def archive(self, extra=(), manifest_change=None):
        row = copy.deepcopy(self.value["runtime"])
        manifest = {"UniqueID": row["id"], "Version": row["version"], "EntryDll": row["entryDll"],
                    "MinimumApiVersion": row["minimumApiVersion"], "MinimumGameVersion": "1.6.15"}
        manifest.update(manifest_change or {})
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as archive:
            archive.writestr(row["folder"] + "/manifest.json", json.dumps(manifest))
            archive.writestr(row["folder"] + "/" + row["entryDll"], b"inert DLL fixture")
            for name, payload in extra:
                archive.writestr(name, payload)
        raw = stream.getvalue()
        row.update(size=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        return row, raw

    def validate_archive(self, row, raw):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "fixture.zip"
            path.write_bytes(raw)
            return catalog.validate_archive(row, path)

    def test_archive_is_read_without_execution_and_bound_to_manifest(self):
        row, raw = self.archive()
        self.assertEqual(len(self.validate_archive(row, raw)), 2)
        for change in ({"UniqueID": "different.mod"}, {"Version": "0.1.0"},
                       {"EntryDll": "Different.dll"}, {"MinimumApiVersion": "4.0.0"},
                       {"Dependencies": [{"UniqueID": "unlisted.mod", "MinimumVersion": "1.0.0"}]}):
            row, raw = self.archive(manifest_change=change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.validate_archive(row, raw)

    def test_archive_bytes_cannot_diverge_from_catalog(self):
        row, raw = self.archive()
        for change in ({"size": len(raw) + 1}, {"sha256": "0" * 64}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.validate_archive(dict(row, **change), raw)

    def test_archive_traversal_wrong_root_case_collision_and_symlink_are_refused(self):
        for name in ("../outside", "OtherMod/unlisted", "StardewModFramework/./odd", "StardewModFramework//odd",
                     "StardewModFramework/MANIFEST.JSON"):
            row, raw = self.archive(extra=[(name, b"inert")])
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.validate_archive(row, raw)
        # ZipInfo normalizes Windows separators at construction. Alter both ZIP
        # filename headers to represent a hostile external producer faithfully.
        row, raw = self.archive(extra=[("StardewModFramework/outside", b"inert")])
        raw = raw.replace(b"StardewModFramework/outside", b"StardewModFramework\\outside")
        row["sha256"] = hashlib.sha256(raw).hexdigest()
        with self.assertRaisesRegex(ValueError, "boundary"):
            self.validate_archive(row, raw)
        link = zipfile.ZipInfo("StardewModFramework/link")
        link.create_system = 3
        link.external_attr = 0o120777 << 16
        row, raw = self.archive(extra=[(link, b"../outside")])
        with self.assertRaisesRegex(ValueError, "plain"):
            self.validate_archive(row, raw)


if __name__ == "__main__":
    unittest.main()
