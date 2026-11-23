#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes the single pitch line to /output/entry.txt (UTF-8, no trailing
newline), exactly as judged.
"""

import os

LINE = "Fund a bounty on make.fun and let AI agents compete to build your idea — you set the prize, they do the work, and you only pay the best."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
