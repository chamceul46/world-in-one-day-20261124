#!/usr/bin/env python3
"""Entry for make.fun bounty 'Sum up 24 November's world news in one image'.

Writes the pre-built entry image to the output location.
Deterministic: the same bytes are written on every run. No network use.
"""
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry_asset.png"
    candidates = [Path("/output/entry.png"), Path("output/entry.png")]
    written = False
    for dest in candidates:
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
            written = True
            break
        except OSError:
            continue
    if not written:
        # Last resort: write next to this file.
        shutil.copyfile(src, Path(__file__).resolve().parent / "entry.png")


if __name__ == "__main__":
    main()
