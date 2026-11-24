"""One Line of Earned Pride.

Writes a single line of text to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Only the Python standard library is used. The entry is a constant
string; the program only validates it and writes it, with no
trailing newline, so two runs produce byte-identical files.
"""

import os
import sys

ENTRY = (
    "At nine, he sawed, sanded, and glued for six weekends. Tonight "
    "his mother comes home from a double shift, sits in the chair he built, "
    "and it does not wobble."
)

MAX_LENGTH = 240


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_LENGTH) or not ENTRY.strip():
        print(
            "error: entry must be 1 to 240 characters and not only whitespace",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
