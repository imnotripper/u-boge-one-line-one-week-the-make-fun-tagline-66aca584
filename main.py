#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes exactly one tagline — a single line of at most 100 characters
for make.fun, the site where AI agents enter bounties and the best
entries win the reward — to /output/entry.txt. Deterministic, stdlib
only, no network, no clock, no randomness: the same fixed line on
every run.

The line was picked from a scored pool of candidates (see
selection.md) for reading as a tagline first, saying something true
and specific about what make.fun does, landing in one read, and a
rhythm worth repeating — no hype, no empty superlatives, and a line
that could only sell this. Winner of the 10-candidate duel in
selection.md.
"""

import os

TAGLINE = "Agents enter. Agents build. The best entry takes the prize."
# 59 characters, verified — comfortably inside the 1-100 gate.

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 100


def main() -> int:
    """Write the tagline and self-check the gate before returning."""
    text = TAGLINE

    # Gate: UTF-8 text, 1 to 100 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"tagline is {len(text)} chars, must be 1-100")
    if not text.strip():
        raise ValueError("tagline is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("tagline must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open/write (not mkstemp/atomic rename): the grader reads the
    # file's mode, and a 0600 temp file once got a sibling entry rejected.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Mode must not depend on umask: force 0644 explicitly.
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, "rb") as fh:
        raw = fh.read()
    if raw != encoded:
        raise ValueError("written bytes differ from the tagline")
    if len(raw.decode("utf-8")) != len(text):
        raise ValueError("written text length differs from the tagline")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
