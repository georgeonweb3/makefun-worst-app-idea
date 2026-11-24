#!/usr/bin/env python3
"""Rent-a-Grandma: the worst app idea ever pitched.

One sentence, 151 characters, pitching the worst, most useless app
imaginable: a product that sounds real, a founder who sounds certain,
and a function nobody on earth needs.

The program writes the pitch to /output/entry.txt. No network, no
arguments, no dependencies beyond the standard library.
"""

import os

PITCH = (
    "Rent-a-Grandma charges $19 an hour for a retired stranger named "
    "Brenda to call you at dinner, ask why you are still single, "
    "and hang up before dessert."
)

MAX_CHARS = 240


def main() -> None:
    pitch = PITCH.strip()
    if not pitch:
        raise SystemExit("pitch must not be empty")
    if len(pitch) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(pitch)} chars, over the 240 limit")

    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file,
    # so the file must hold exactly the 151-character pitch, nothing more.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(pitch)

    print(f"wrote {len(pitch)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
