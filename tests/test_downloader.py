# ==== Imports ==== #
from pathlib import Path
from unittest.mock import patch
from audiograb.core.downloader import download

import pytest


def test_creates_output_directory(tmp_path: Path) -> None:
    output_dir = tmp_path / "Audiograb downloads"
    with patch("audiograb.core.downloader.yt_dlp") as mock_yt_dlp:
        download("http://why-are-you-seeing-the-test-files-?.com", output_dir)
        assert output_dir.exists()
