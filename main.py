"""One Line, One Chill — make.fun entry (Account B / one-chill-B).

Writes a single sentence of horror to /output/entry.txt.

The line: a quiet body-horror twist. A routine dental visit turns up
something that should not exist — a second set of teeth, already at work.
No mirror, no doll, no basement: the scare is the implication that
whatever is growing behind the narrator's own teeth is already eating.
"""

from pathlib import Path

# The entry: one sentence, one line, under 200 characters.
ENTRY = "The dentist found a second set of teeth growing behind mine, and they were already chewing."

# Where the gate expects the entry.
OUTPUT_PATH = Path("/output/entry.txt")

# Gate limits from RULES.txt: 1 to 200 characters, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 200


def verify(text: str) -> None:
    """Enforce the gate from RULES.txt, raising on any violation."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if text.count("\n") != 0:
        raise ValueError("entry must be a single line")


def write_entry(path: Path = OUTPUT_PATH) -> str:
    """Verify the entry and write it to the gate's output path."""
    verify(ENTRY)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")
    return ENTRY


def main() -> None:
    text = write_entry()
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
