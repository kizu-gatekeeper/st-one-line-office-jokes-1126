"""Entry for make.fun: One-Line Office Jokes.

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: the current directory), with no trailing newline.
"""
import os

LINE = "The office printer has printed four thousand pages flawlessly this year, and every single one was a test page nobody asked for."
MAX_CHARS = 199


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
