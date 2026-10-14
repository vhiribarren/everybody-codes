#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

from pathlib import Path
from itertools import batched

INPUT_FILEPATH = (p := Path(__file__)).parent/".."/"inputs"/f"{p.stem}.txt"


VALUES = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

def solver(input_data: str):
    points = 0
    for c in batched(input_data, n=2):
        points += 2 if not 'x' in c else 0
        points += sum(VALUES.get(d, 0) for d in c)
    print("Result:", points)


if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
