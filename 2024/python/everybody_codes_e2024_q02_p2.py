#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

from pathlib import Path

INPUT_FILEPATH = (p := Path(__file__)).parent/".."/"inputs"/f"{p.stem}.txt"


def solver(input_data: str):
    lines = input_data.splitlines()
    words = lines[0].split(":")[1].split(",")
    text = " ".join(lines[2:])
    rev_text = text[::-1]
    rune_indices = set()
    for idx in range(len(text)):
        for w in words:
            if text[idx:].startswith(w):
                rune_indices |= set(range(idx, idx+len(w)))
            if rev_text[idx:].startswith(w):
                rune_indices |= set(range(len(text)-1-idx, len(text)-1-idx-len(w), -1))                
    print("Result:", len(rune_indices))


if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
