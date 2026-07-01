#!/usr/bin/env python3
"""Tiny dependency-free token-ish counter for AI demo scaffolding.

This is not a real tokenizer. It is a simple approximation useful for slides,
live demos, and explaining why prompt size matters.
"""

from __future__ import annotations

import re
import sys


def rough_tokens(text: str) -> int:
    """Approximate token count with a word/punctuation split."""
    return len(re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE))


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        text = " ".join(argv[1:])
    else:
        text = sys.stdin.read()

    chars = len(text)
    words = len(re.findall(r"\w+", text, flags=re.UNICODE))
    tokens = rough_tokens(text)

    print(f"characters: {chars}")
    print(f"words:      {words}")
    print(f"~tokens:    {tokens}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
