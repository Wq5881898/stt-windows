import json
import tempfile
import unittest
import os
from pathlib import Path
from unittest.mock import patch

from packages.shared_core import key_management as keys
from packages.shared_core import media_pipeline as pipeline


class TranslationConfigurationTests(unittest.TestCase):
    def test_empty_release_template_is_not_reported_as_a_key(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "gladia_keys.txt"
            path.write_text("# Add your key here\n", encoding="utf-8")
            with patch.object(pipeline, "GLADIA_KEYS_PATH", path), patch.dict(os.environ, {"GLADIA_API_KEY": ""}):
                checks = pipeline.collect_environment_checks(needs_translation=False, needs_video_tools=False)
            self.assertFalse(next(check for check in checks if check.name == "gladia").ok)

    def test_custom_endpoint_and_model_survive_key_change(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "qwen.json"
            keys.write_translation_key("qwen", "first", path, base_url="https://example.com/v1/", model="qwen-custom")
            keys.write_translation_key("qwen", "second", path)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved, {"api_key": "second", "base_url": "https://example.com/v1", "model": "qwen-custom"})

    def test_key_check_uses_unsaved_form_endpoint_and_model(self):
        with patch.object(keys, "_request_json", return_value=(200, {"choices": [{"message": {"content": "OK"}}]})) as request:
            result = keys.check_translation_key("qwen", "test-value", base_url="https://example.com/v1", model="custom")
        self.assertTrue(result.valid)
        sent = request.call_args.args[0]
        self.assertEqual(sent.full_url, "https://example.com/v1/chat/completions")
        self.assertEqual(json.loads(sent.data)["model"], "custom")


if __name__ == "__main__":
    unittest.main()
