"""Entry for make.fun: The GPS Swears It Was a Shortcut.

Writes the GPS's own one-line excuse to entry.txt.
"""

import os

ENTRY = "Blame the map, not me: it promised me a shortcut through the lake, and the wedding guests still think your headlights were part of the ceremony."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
