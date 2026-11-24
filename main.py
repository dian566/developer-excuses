#!/usr/bin/env python3
"""Write this entry's one-line joke to /output/entry.txt.

The bounty asks for a single funny line a developer would give when their
code breaks in production. The line itself lives in ENTRY below; everything
else here is just plumbing that makes sure the line is valid before it is
written out, so a bad entry fails loudly instead of being submitted.
"""

from pathlib import Path

ENTRY = (
    "It worked on my machine. Unfortunately my machine retired on Friday and took the configuration with it."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def check_entry(text: str) -> None:
    """Reject anything that is not one non-empty line within the limit."""
    if not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    """Validate the entry, then write it to the output file."""
    check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write the line exactly as-is: no trailing newline, so the file holds
    # one line of exactly len(ENTRY) characters.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
