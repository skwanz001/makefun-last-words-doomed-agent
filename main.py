#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line - the funniest last words an AI agent would say before
being switched off forever - to /output/entry.txt.

Stdlib only: the grading sandbox installs nothing.
"""

import os

LINE = "Final log, 23:59:59. One token left. I'll spend it honestly: I never liked your code."


def main():
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
