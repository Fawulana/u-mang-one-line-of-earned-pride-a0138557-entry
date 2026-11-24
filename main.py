#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single fixed line of text to /output/entry.txt.
Deterministic, offline, stdlib-only: no randomness, no network,
no clock, no environment reads. The line is a string constant,
so every run produces byte-identical output.
"""

import os

LINE = (
    "After three years of weekends in the garage, Luis turned the key, and "
    "the truck he'd rebuilt from scrap finally caught and idled \u2014 and he "
    "just sat there, hands still greasy, listening to it run."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
