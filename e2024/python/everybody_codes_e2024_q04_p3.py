#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

from pathlib import Path

INPUT_FILEPATH = (p := Path(__file__)).parent/".."/"inputs"/f"{p.stem}.txt"

def solver(input_data: str):
    nails = list(map(int, input_data.splitlines()))
    candidates = []
    for base_nail in nails:
        candidates.append(sum(abs(nail - base_nail) for nail in nails))
    result = min(candidates)
    print("Result:", result)

if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
