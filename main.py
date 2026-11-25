"""Write the phone's last text at one percent battery to /output/entry.txt."""

from pathlib import Path

# The entry is exactly this one text message: no trailing newline, nothing else.
ENTRY_TEXT = "u up? no. i'm down. 1%. tell them i died doing what i loved: ignoring low battery warnings"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
