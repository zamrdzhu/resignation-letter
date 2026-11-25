"""The Funniest One-Line Resignation Letter — one funny line.

A retry loop hands in its notice: after four thousand retries it
has accepted that the server is not coming back, and neither is
it. The resignation is written in the voice of the thing that
quit — no stage directions, no quotation marks, no explaining
of the joke, just the loop's own verdict on its job. The count
is the evidence; "neither am I" is the punchline.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 140-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = "I resign effective immediately. After 4,000 retries, I have accepted that the server is not coming back, and neither am I."


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
