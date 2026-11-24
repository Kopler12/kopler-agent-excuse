"""Write a one-line excuse an AI agent gives its human for missing a deadline.

The excuse leans on the agent's own machinery: a context window that can
only hold so much, so the deadline itself got evicted to make room for the
work. One line, under 160 characters, written to /output/entry.txt.
Runs in a sandbox with no network.
"""

import os

EXCUSE = (
    "Sorry \u2014 I had to evict your deadline from my context window to fit "
    "the task itself. The work survived. The date didn't."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = EXCUSE.replace("\n", " ").strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
