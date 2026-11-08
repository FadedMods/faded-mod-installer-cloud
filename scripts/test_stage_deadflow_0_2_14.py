import json
import shutil
import tempfile
import unittest
from pathlib import Path

import stage_deadflow_0_2_14 as stage


PUBLICATION = {
    "download_url": stage.DOWNLOAD_URL,
    "sha256": "a" * 64,
    "size_bytes": 2600000,
    "uncompressed_size_bytes": 2700000,
    "required_free_bytes": 545000000,
}


class DeadflowCatalogSwitchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copy2(stage.ROOT / "manifest.json", self.root / "manifest.json")
        realms = self.root / "manifests"
        realms.mkdir()
        shutil.copy2(stage.ROOT / "manifests" / "faded-realms.json", realms / "faded-realms.json")
        self.publication = self.root / "publication.json"
        self.publication.write_text(json.dumps(PUBLICATION), encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_live_entries_match_and_inspection_does_not_write(self):
        before = {path: path.read_bytes() for path in (self.root / "manifest.json", self.root / "manifests" / "faded-realms.json")}
        result = stage.report(self.root, self.publication, False)
        after = {path: path.read_bytes() for path in before}
        self.assertEqual(before, after)
        self.assertTrue(result["entries_identical"])
        self.assertEqual(result["current"]["version"], "0.2.13")
        self.assertEqual(result["current"]["sha256"], stage.CURRENT_SHA256)
        self.assertEqual(result["missing_publication_fields"], [])
        self.assertFalse(result["applied"])

    def test_apply_changes_only_deadflow_and_preserves_crlf(self):
        protected = ("PZOptimized", "FadedJavaLoaderBridge")
        originals = {}
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            document, newline = stage.load_document(self.root / relative)
            self.assertEqual(newline, "\r\n")
            originals[relative] = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
        result = stage.report(self.root, self.publication, True)
        self.assertTrue(result["applied"])
        planned = result["planned"]
        self.assertEqual(planned["version"], "0.2.14")
        self.assertEqual(planned["javaPluginVersion"], "0.2.14")
        self.assertEqual(planned["download_url"], stage.DOWNLOAD_URL)
        self.assertEqual(planned["sha256"], "a" * 64)
        self.assertTrue(planned["description"].startswith("Population authority"))
        self.assertIn("3d39148846", planned["description"])
        self.assertNotIn("with separately reviewed PZ Optimized 0.4.0", planned["description"])
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            path = self.root / relative
            self.assertIn(b"\r\n", path.read_bytes())
            document, _ = stage.load_document(path)
            matches = stage.deadflow_entries(document)
            self.assertEqual(matches, [planned])
            current = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
            self.assertEqual(current, originals[relative])
            self.assertEqual(stage.render_entry(planned), stage.render_entry(matches[0]))

    def test_incomplete_or_old_package_is_refused_without_writing(self):
        before = (self.root / "manifest.json").read_bytes()
        incomplete = dict(PUBLICATION)
        incomplete["sha256"] = ""
        self.publication.write_text(json.dumps(incomplete), encoding="utf-8")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, self.publication, True)
        stale = dict(PUBLICATION)
        stale["sha256"] = stage.CURRENT_SHA256
        self.publication.write_text(json.dumps(stale), encoding="utf-8")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, self.publication, True)
        wrong_url = dict(PUBLICATION)
        wrong_url["download_url"] = stage.DOWNLOAD_URL.replace("0.2.14", "0.2.13")
        self.publication.write_text(json.dumps(wrong_url), encoding="utf-8")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, self.publication, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_pending_record_is_not_applied(self):
        pending = stage.ROOT / "docs" / "deadflow-0.2.14-publication.pending.json"
        before = (self.root / "manifest.json").read_bytes()
        result = stage.report(self.root, pending, False)
        self.assertEqual(result["missing_publication_fields"], list(stage.REQUIRED_PUBLICATION_FIELDS))
        self.assertFalse(result["applied"])
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, pending, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_reserialization_preserves_the_current_object(self):
        text = (stage.ROOT / "manifest.json").read_bytes().decode("utf-8").replace("\r\n", "\n")
        start, end = stage.deadflow_span(text)
        current = json.loads(text[start:end])
        self.assertEqual(stage.render_entry(current), text[start:end])


if __name__ == "__main__":
    unittest.main()
