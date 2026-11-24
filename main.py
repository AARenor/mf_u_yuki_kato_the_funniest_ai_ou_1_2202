#!/usr/bin/env python3
"""Write the make.fun out-of-office entry text to entry.txt.

The whole entry is one short line of text. This program writes exactly those
bytes (UTF-8, no trailing newline) into the output folder and reports the
character count on stderr.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry must be 1-280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
