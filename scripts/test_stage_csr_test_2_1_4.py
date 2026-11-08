import json
import shutil
import tempfile
import unittest
from pathlib import Path

import stage_csr_test_2_1_4 as stage


PUBLICATION = {
    "download_url": stage.DOWNLOAD_URL,
    "sha256": "c" * 64,
    "size_bytes": 96000000,
    "uncompressed_size_bytes": 254000000,
    "required_free_bytes": 890000000,
}


class CsrTestCatalogSwitchTests(unittest.TestCase):
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
        self.assertEqual(before, {path: path.read_bytes() for path in before})
        self.assertTrue(result["entries_identical"])
        self.assertEqual(result["current"]["version"], "2.1.4")
        self.assertEqual(result["current"]["sha256"], stage.CURRENT_SHA256)
        self.assertIs(result["current"]["requiresJavaLoader"], False)
        self.assertEqual(result["missing_publication_fields"], [])
        self.assertFalse(result["applied"])

    def test_apply_changes_only_the_test_entry_and_preserves_crlf(self):
        protected = ("CommonSenseReborn", "Deadflow", "PZOptimized", "FadedJavaLoaderBridge")
        originals = {}
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            document, newline = stage.load_document(self.root / relative)
            self.assertEqual(newline, "\r\n")
            originals[relative] = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
        result = stage.report(self.root, self.publication, True)
        planned = result["planned"]
        self.assertEqual(planned["version"], "2.1.4")
        self.assertEqual(planned["download_url"], stage.DOWNLOAD_URL)
        self.assertEqual(planned["sha256"], "c" * 64)
        self.assertIn("3d39148846", planned["description"])
        self.assertIs(planned["requiresJavaLoader"], False)
        self.assertFalse(any(key.startswith("java") for key in planned))
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            path = self.root / relative
            self.assertIn(b"\r\n", path.read_bytes())
            document, _ = stage.load_document(path)
            self.assertEqual(stage.entries(document), [planned])
            current = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
            self.assertEqual(current, originals[relative])

    def test_incomplete_old_or_wrong_url_is_refused_without_writing(self):
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
        wrong = dict(PUBLICATION)
        wrong["download_url"] = stage.DOWNLOAD_URL.replace("2.1.4", "2.1.3")
        self.publication.write_text(json.dumps(wrong), encoding="utf-8")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, self.publication, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_confirmed_record_is_already_published_and_does_not_rewrite(self):
        pending = stage.ROOT / "docs" / "csr-test-2.1.4-publication.pending.json"
        before = (self.root / "manifest.json").read_bytes()
        result = stage.report(self.root, pending, False)
        self.assertEqual(result["missing_publication_fields"], [])
        self.assertEqual(result["current"]["sha256"], "10ef8f347b716e4c9fa660d3dad2ee6d09527daa120262b350028ab5db5b4eb2")
        self.assertEqual(result["current"]["size_bytes"], 95362016)
        self.assertEqual(result["current"]["uncompressed_size_bytes"], 253919656)
        self.assertEqual(result["current"]["required_free_bytes"], 886152584)
        self.assertIs(result["current"]["requiresJavaLoader"], False)
        self.assertFalse(any(key.startswith("java") for key in result["current"]))
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, pending, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_reserialization_preserves_the_current_object(self):
        text = (stage.ROOT / "manifest.json").read_bytes().decode("utf-8").replace("\r\n", "\n")
        start, end = stage.entry_span(text)
        current = json.loads(text[start:end])
        self.assertEqual(stage.render_entry(current), text[start:end])


if __name__ == "__main__":
    unittest.main()
