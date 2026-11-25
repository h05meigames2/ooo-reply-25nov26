#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single funny out-of-office auto-reply line to entry.txt.
Deterministic: the exact same line on every run.
"""

import os

REPLY = "I'm away — my inbox is in charge, and it has no experience and even less patience."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
