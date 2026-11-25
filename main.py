#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge -- make.fun entry.

Writes one line (<= 200 characters) to <output>/entry.txt: a note the
smart fridge leaves for its owner -- the leftovers have unionized.
"""

import os
import sys

# The line: the leftovers from March have unionized and sent a message
# through the fridge -- a petty, domestic grudge with a sting the reader
# does not see coming ("they are not 'still good'" answers the owner's
# own excuse back at them). 94 characters, one line.
LINE = "The leftovers from March have unionized. They asked me to tell you: they are not 'still good'."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes, no trailing
    # newline, and the character count the gate will see.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    assert not data.endswith(b"\n"), "entry must be a single line, no trailing newline"
    assert len(text.encode("utf-8")) <= 200, "entry over 200 bytes"
    print(text)
    print(f"({len(text)} characters)", file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
