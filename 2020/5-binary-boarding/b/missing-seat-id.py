from pathlib import Path
from typing import List


def find_row(ticket: str):
    # F: front : lower half
    # B: back : upper half
    min = 0
    max = 127
    for step in ticket:
        half = (max - min + 1) // 2
        if step == 'F':
            max -= half
        elif step == 'B':
            min += half
    return min


def find_col(ticket: str):
    # L: left : lower half
    # R: right : upper half
    min = 0
    max = 7
    for step in ticket:
        half = (max - min + 1) // 2
        if step == 'L':
            max -= half
        elif step == 'R':
            min += half
    return min


path = (Path(__file__).parent / "./input").resolve()
with open(path, 'r') as fp:
    tickets = fp.read().splitlines()
    ids: List[int] = []
    for ticket in tickets:
        row = find_row(ticket[:7])
        column = find_col(ticket[7:])
        ids.append(row * 8 + column)

    # finding the missing seat should just mean cycling through the sorted list of all ids until you find a gap
    ids.sort()
    for i in range(1, len(ids)):
        if ids[i] != ids[i-1] + 1:
            # Found a gap
            print(ids[i-1] + 1)
            break
