# SPDX-License-Identifier: MIT
"""Write one debugging haiku to /output/entry.txt.

The haiku is three fixed lines in the 5-7-5 syllable shape: a red line in
the log, one small change and a prayer, and it works but nobody knows why.
It is written to /output/entry.txt (or the directory named by
MAKEFUN_OUTPUT_DIR) as UTF-8, 1 to 200 characters (the text is 77 characters),
never only whitespace. No network, no randomness, no arguments. The
output directory is created if missing and never deleted.
"""

import os
import sys

TEXT = (
    "red line in the log\n"
    "I change one small thing and pray\n"
    "it works, don't ask why"
)

# A short, known-valid haiku used only if TEXT ever failed the gate.
FALLBACK = (
    "a stack trace at dawn\n"
    "a missing comma broke it\n"
    "now the tests are green"
)


def valid(text: str) -> bool:
    """Competition gate: 1-200 characters, not only whitespace."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def choose_text() -> str:
    if valid(TEXT):
        return TEXT
    if valid(FALLBACK):
        return FALLBACK
    print("error: no valid entry text available", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    text = choose_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
