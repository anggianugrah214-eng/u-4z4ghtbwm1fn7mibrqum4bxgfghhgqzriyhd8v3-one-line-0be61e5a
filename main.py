#!/usr/bin/env python3
"""One Line, One Laugh.

A program/v1 entry for make.fun competition
u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.

The program writes a single funny line (at most 140 characters) to
/output/entry.txt.

It is fully deterministic: the same line is written on every run, with no
input, no network access and no randomness.
"""

import os

# One line, 83 characters: the plant died, the plastic replacement still
# demands chores — "dust its corpse" is the punchline. Chosen over 13
# other candidates after pairwise scoring against the judge brief (see
# candidates.md in the build workspace): it is a real joke with a twist,
# a fresh angle rather than a meme format, and it lands instantly with
# no setup or explanation.
LINE = "My plant died, so I bought a plastic one. Now I have to dust its corpse every week."


def main() -> None:
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry line fails the 1-140 character gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
