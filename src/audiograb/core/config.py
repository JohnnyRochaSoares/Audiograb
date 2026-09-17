import json
from pathlib import Path

from platformdirs import user_config_dir

path = Path(user_config_dir("audiograb"))

path.mkdir(parents=True, exist_ok=True)

settings_file = path / "settings.json"


def save_download_folder(folder: Path) -> None:
    settings = {
        "download_folder": str(folder),
    }

    with open(settings_file, "w", encoding="utf-8") as settings_json:
        json.dump(settings, settings_json, indent=4)
