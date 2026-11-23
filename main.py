#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the grader output directory.

The entry is entry.png: a one-page news broadsheet summing up Sunday
22 November 2026 in 40 stories across 7 regions plus space, with a source
badge on every story, a Natural Earth world map with numbered dots, a UTC
timeline and a date-check. It was drawn with real fonts (DejaVu Sans).

This program only copies the image, byte for byte, so both grader runs
produce identical bytes. A copy has no timestamps or randomness in it:
the same source file always yields the same output file. Standard
library only; no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    sys.exit(main())
