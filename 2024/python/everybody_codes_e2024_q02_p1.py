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
    result = sum(lines[2].count(w) for w in words)
    print("Result:", result)


if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
