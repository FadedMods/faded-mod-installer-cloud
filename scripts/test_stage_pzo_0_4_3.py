import json
import shutil
import tempfile
import unittest
from pathlib import Path

import stage_pzo_0_4_3 as stage


PUBLICATION = {
    "download_url": stage.DOWNLOAD_URL,
    "sha256": "b" * 64,
    "size_bytes": 251863885,
    "uncompressed_size_bytes": 266476534,
    "required_free_bytes": 1055211331,
}


class PzoCatalogSwitchTests(unittest.TestCase):
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
        self.assertEqual(result["current"]["version"], "0.4.3")
        self.assertEqual(result["current"]["sha256"], stage.CURRENT_SHA256)
        self.assertEqual(result["current"]["minimumJavaLoaderVersion"], "0.6.10")
        self.assertEqual(result["missing_publication_fields"], [])
        self.assertFalse(result["applied"])

    def test_apply_changes_only_pz_optimized_and_preserves_crlf(self):
        protected = ("Deadflow", "FadedJavaLoaderBridge")
        originals = {}
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            document, newline = stage.load_document(self.root / relative)
            self.assertEqual(newline, "\r\n")
            originals[relative] = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
        result = stage.report(self.root, self.publication, True)
        self.assertTrue(result["applied"])
        planned = result["planned"]
        self.assertEqual(planned["version"], "0.4.3")
        self.assertEqual(planned["javaPluginVersion"], "0.4.3")
        self.assertEqual(planned["minimumJavaLoaderVersion"], "0.6.10")
        self.assertEqual(planned["download_url"], stage.DOWNLOAD_URL)
        self.assertEqual(planned["sha256"], "b" * 64)
        self.assertEqual(planned["size_bytes"], 251863885)
        self.assertEqual(planned["uncompressed_size_bytes"], 266476534)
        self.assertEqual(planned["required_free_bytes"], 1055211331)
        self.assertIn("3d39148846", planned["description"])
        self.assertNotIn("0.4.2 supports", planned["description"])
        for relative in ("manifest.json", "manifests/faded-realms.json"):
            path = self.root / relative
            self.assertIn(b"\r\n", path.read_bytes())
            document, _ = stage.load_document(path)
            matches = stage.entries(document)
            self.assertEqual(matches, [planned])
            current = {mod["id"]: mod for mod in document["mods"] if mod.get("id") in protected}
            self.assertEqual(current, originals[relative])
            self.assertEqual(stage.render_entry(planned), stage.render_entry(matches[0]))

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
        wrong_url = dict(PUBLICATION)
        wrong_url["download_url"] = stage.DOWNLOAD_URL.replace("0.4.3", "0.4.2")
        self.publication.write_text(json.dumps(wrong_url), encoding="utf-8")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, self.publication, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_confirmed_record_is_already_published_and_does_not_rewrite(self):
        record = stage.ROOT / "docs" / "pzo-0.4.3-publication.json"
        before = (self.root / "manifest.json").read_bytes()
        result = stage.report(self.root, record, False)
        self.assertEqual(result["missing_publication_fields"], [])
        self.assertEqual(result["current"]["sha256"], "4460ce81890358c6a3a36e053757bc56b6a0035a6c240e1d870d24da04a9e166")
        self.assertEqual(result["current"]["size_bytes"], 251863885)
        self.assertEqual(result["current"]["uncompressed_size_bytes"], 266476534)
        self.assertEqual(result["current"]["required_free_bytes"], 1055211331)
        self.assertEqual(result["current"]["minimumJavaLoaderVersion"], "0.6.10")
        with self.assertRaises(stage.CatalogError):
            stage.report(self.root, record, True)
        self.assertEqual((self.root / "manifest.json").read_bytes(), before)

    def test_reserialization_preserves_the_current_object(self):
        text = (stage.ROOT / "manifest.json").read_bytes().decode("utf-8").replace("\r\n", "\n")
        start, end = stage.entry_span(text)
        current = json.loads(text[start:end])
        self.assertEqual(stage.render_entry(current), text[start:end])


if __name__ == "__main__":
    unittest.main()
