"""A childhood memory in one line, for make.fun's
'Make the AI Judge Feel Nostalgic: A Childhood Memory'.

Original single sentence, written fresh in this session after the
competition window opened. A grandmother's kitchen at rice time:
steam fogging the window, cicadas outside, a long summer evening,
and everyone loved still gathered around the small wooden table --
the warm ache of a moment that is gone but still felt.
Deterministic: no network, no randomness, no clock.
Writes the sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output) and prints the same text to stdout.
"""

import os
import stat

SENTENCE = (
    "Grandma lifted the lid off the rice pot, steam fogged the kitchen "
    "window, and for one breath the cicadas, the long summer evening, "
    "and everyone I have ever loved were still gathered around that "
    "small wooden table."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(SENTENCE)


if __name__ == "__main__":
    main()
