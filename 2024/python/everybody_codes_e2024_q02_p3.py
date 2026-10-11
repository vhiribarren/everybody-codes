#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

from pathlib import Path

INPUT_FILEPATH = (p := Path(__file__)).parent/".."/"inputs"/f"{p.stem}.txt"

type Coords = tuple[int, int]


def solver(input_data: str):
    lines = input_data.splitlines()
    words = lines[0].split(":")[1].split(",")
    grid = {
        (x, y): c
        for (y, line) in enumerate(lines[2:])
        for (x, c) in enumerate(line)
    }
    width = len(lines[2])
    height = len(lines[2:])
    scales = set[Coords]()
    for x in range(width):
        for y in range(height):
            for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
                for word in words:
                    coords = [((x + dir[0]*idx) % width, y + dir[1]*idx)
                              for idx in range(len(word))]
                    for w, c in zip(word, coords):
                        if not c in grid or w != grid[c]:
                            break
                    else:
                        scales |= set(coords)
    print("Result:", len(scales))

if __name__ == "__main__":
    file_data = INPUT_FILEPATH.read_text()
    solver(file_data)
