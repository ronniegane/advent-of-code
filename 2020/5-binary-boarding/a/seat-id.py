from pathlib import Path


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
    maxID = 0
    for ticket in tickets:
        row = find_row(ticket[:7])
        column = find_col(ticket[7:])
        id = row * 8 + column
        # print('ticket: %s row: %d col: %d id: %d' % (ticket, row, column, id))
        if id > maxID:
            maxID = id
    print(maxID)
