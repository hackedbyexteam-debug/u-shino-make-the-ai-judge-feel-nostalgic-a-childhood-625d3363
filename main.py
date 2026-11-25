#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence, at most 280 characters, to /output/entry.txt
(program/v1 harness). The gate requires UTF-8 text of 1 to 280
characters, so the length guard below fails loudly instead of
shipping an invalid entry.

The sentence: learning to ride a bike, the father's hand on the
seat, and the moment the child realises he has already let go —
concrete place (cracked pavement behind the flat), concrete
sensation (laughing instead of panting), small honest detail,
and the warm ache of a letting-go that only lands years later.
"""

import os

MESSAGE = (
    "I learned to ride my bike on the cracked pavement behind our flat, "
    "my father running behind me with one hand on the seat, and I only "
    "realised he had let go when I heard him laughing instead of panting."
)


def main() -> None:
    if not 1 <= len(MESSAGE) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(MESSAGE)}")
    # Single-sentence guard: exactly one sentence terminator, the final
    # full stop. A second sentence would break the bounty brief.
    if MESSAGE.count(".") != 1 or not MESSAGE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
