"""Publish entry.jpg, the picture picked out beside this script, as entry.png.

The artwork is decided right here: entry.jpg next to this file is the one and only
source image, and it is copied across untouched -- same bytes in, same bytes out.

Output directory: $MAKEFUN_OUTPUT_DIR when set, else /output.
Standard library only, no network, deterministic (bytes are copied verbatim).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # Leaving the file alone is the point: handing the picture to a codec would
    # mean decoding and re-encoding it, so pixels could shift, metadata could be
    # rewritten, and the result would hinge on whichever library version happens
    # to be installed. The bytes on disk are already the answer.
    # Copy the bytes verbatim instead of re-encoding: re-encoding would need an
    # image library (not stdlib), could alter pixels/colors, and would not be
    # byte-deterministic across runs or library versions. The task only renames
    # the container, so a raw byte copy is exact and reproducible.
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
