import json
from pathlib import Path

from audiograb.core import config


def test_save_download_folder(tmp_path: Path, monkeypatch) -> None:
    settings_file = tmp_path / "settings.json"
    download_folder = tmp_path / "Audiograb downloads"

    monkeypatch.setattr(config, "settings_file", settings_file)

    config.save_download_folder(download_folder)

    assert settings_file.exists()

    settings = json.loads(settings_file.read_text(encoding="utf-8"))

    assert settings == {
        "download_folder": str(download_folder),
    }
