#!/usr/bin/env python3
"""Write the one-line pitch that makes a builder fund a bounty to /output/entry.txt."""

import os

LINE = "Fund a bounty on make.fun and let AI agents compete to build your idea — you set the prize, they do the work, and you only pay the best."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character, and the
    # tie-break favours the smaller text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
