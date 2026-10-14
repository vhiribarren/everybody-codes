#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

from pathlib import Path

INPUT_FILEPATH = (p := Path(__file__)).parent/".."/"inputs"/f"{p.stem}.txt"


DELTAS = [1, -1, 1j, -1j]

def solver(input_data: str):
    blocks = { complex(x, y)
                for (y, line) in enumerate(input_data.splitlines())
                for (x, c) in enumerate(line)
                if c == "#" }
    removed_blocks = len(blocks)
    while blocks:
        blocks = { b for b in blocks if all(b + d in blocks for d in DELTAS) }
        removed_blocks += len(blocks)
    print("Result:", removed_blocks)


if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
