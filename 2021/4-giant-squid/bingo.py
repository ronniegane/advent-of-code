import os

"""
How to handle bingo playing?
What sort of data structure is appropriate here?

Ultra-naive approach:
For each board, build two MxM 2D arrays
one for values
one for marks

for each number called, iterate through the values grids and if found, mark the
corresponding mark grid.

for each number called from the Mth one on, iterate through mark grid
to see if we have a winner

complexity:
N * M * M where N is the number of boards and M is board size

Possible improvements:
calculate a board's score as numbers are drawn:
1. start with score = sum of all numbers on the board (during board creation)
2. subtract a drawn number if matched

more efficient bingo-checking
if we find during column-bingo check that column 2 row 2 is unmarked, don't need to row-check row 2

more efficient crossing-off
should we build a dictionary of value -> position for each board
so we don't have to do an O(N^2) search for values?
"""


def mark_numbers(boards, number):
    for board in boards:
        for i, row in enumerate(board["values"]):
            for j, value in enumerate(row):
                if value == number:
                    board["marks"][i][j] = 1


def find_winners(boards):
    winners = []
    board_size = len(boards[0]["marks"])
    for board in boards:
        for i in range(board_size):
            # Check vertical bingo
            column_bingo = True
            for row in range(board_size):
                if board["marks"][row][i] == 0:
                    column_bingo = False
                    break

            # Check horizontal bingo
            row_bingo = True
            for column in range(board_size):
                if board["marks"][i][column] == 0:
                    row_bingo = False
                    break
            if column_bingo or row_bingo:
                winners.append(board)
                break

    return winners


def calculate_scores(winning_boards):
    for board in winning_boards:
        sum = 0
        for i, row in enumerate(board["marks"]):
            for j, value in enumerate(row):
                if value == 0:
                    sum += board["values"][i][j]
        board["score"] = sum

    winning_boards.sort(key=lambda x: x["score"], reverse=True)
    return winning_boards[0]

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    numbers = [int(x) for x in input.readline().strip().split(",")]
    print(numbers)

    boards = []
    board_index = -1
    # Read boards in
    for line in input:
        # print(line)
        stripline = line.strip()
        if stripline == "":
            # new board starting
            new_board = {"values": [], "marks": []}
            boards.append(new_board)
            board_index += 1
        else:
            boards[board_index]["values"].append([int(x) for x in stripline.split()])
            boards[board_index]["marks"].append([0 for x in stripline.split()])

    # print(boards)

    for i, number in enumerate(numbers):
        print(number)
        # Mark off any boards with matching numbers
        mark_numbers(boards, number)

        # Check for winners
        if i >= len(boards[0]):
            winning_boards = find_winners(boards)
            if len(winning_boards) >= 1:
                print("winner!")
                winning_board = calculate_scores(winning_boards)
                break

    print(winning_boards)
    print(winning_board["score"] * number)
