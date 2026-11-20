"""make.fun news-image-20261120 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a one-page newspaper
front page summing up the world news of Friday 20 November 2026. The
program copies it to /output/entry.png. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT, "entry.png")
shutil.copyfile(src, dst)
# The grader runs the program twice and both runs must write the same
# bytes: fail loudly instead of leaving a partial file behind.
assert os.path.getsize(dst) == os.path.getsize(src) > 0, "entry.png copy failed"
