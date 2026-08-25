# ==== Imports ==== #
from pathlib import Path

import yt_dlp


# ==== Download Function
def download(url: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # type: ignore
        ydl.download([url])
