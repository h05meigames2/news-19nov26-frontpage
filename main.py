#!/usr/bin/env python3
"""Copy the pre-rendered front page to the make.fun output directory.

The grading sandbox runs with the standard library only and no network, so
the image is drawn at build time by gen_image.py and shipped as entry.png.
This program just copies that file to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output), creating the directory when needed.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
