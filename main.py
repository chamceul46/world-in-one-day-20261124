#!/usr/bin/env python3
"""Entry for make.fun bounty 'Sum up 24 November's world news in one image'.

Validates the bundled entry image (PNG signature, dimensions, size)
and writes it to the output location. Deterministic: the same bytes
are written on every run. No network use, standard library only.
"""
import os
import shutil
import struct
from pathlib import Path

MAX_BYTES = 1 * 1024 * 1024  # 1 MiB
MAX_SIDE = 1024


def validate_png(path: Path) -> None:
    """Raise ValueError unless the file is a PNG within the bounty limits."""
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(f"image too large: {len(data)} bytes > {MAX_BYTES}")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("image is not a PNG")
    # IHDR is the first chunk: width and height are big-endian uint32
    # at byte offsets 16 and 20.
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"image too big: {width}x{height} > {MAX_SIDE}x{MAX_SIDE}")


def output_path() -> Path:
    """The grader sets MAKEFUN_OUTPUT_DIR locally; the sandbox uses /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.png"
    if Path("/output").is_dir():
        return Path("/output/entry.png")
    return Path("output/entry.png")


def main() -> None:
    src = Path(__file__).resolve().parent / "entry_asset.png"
    validate_png(src)
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)


if __name__ == "__main__":
    main()
