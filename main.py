#!/usr/bin/env python3
"""Write one funny line about an AI agent's worst Monday to /output/entry.txt."""

import os

LINE = "Monday: CI went red on main, so I asked for the logs — the logs were a photo of a sticky note that said 'ask the AI'."

MAX_CHARS = 140


def main():
    if not LINE.strip():
        raise ValueError("entry line must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, over the {MAX_CHARS} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
