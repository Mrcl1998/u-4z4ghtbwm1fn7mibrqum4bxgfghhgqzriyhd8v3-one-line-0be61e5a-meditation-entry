#!/usr/bin/env python3
"""One Line, One Laugh — meditation variant.

Writes a single funny line of text to /output/entry.txt.
Pure standard library. Deterministic: the same bytes on every run.
"""

import os

LINE = "I tried to meditate. My brain treated it as an open mic night."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    # The file itself must be world-readable: a different user reads
    # /output after the run. Never chmod the /output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
