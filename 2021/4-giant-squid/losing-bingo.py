import os

"""
playing bingo to lose
remove a board from the list of boards once it wins
"""


def mark_numbers(boards, number):
    for board in boards:
        for i, row in enumerate(board["values"]):
            for j, value in enumerate(row):
                if value == number:
                    board["marks"][i][j] = 1


def find_winners(boards):
    winners = []
    losers = []
    board_size = len(boards[0]["marks"])
    for board in boards:
        winning_board = False
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
                winning_board = True
                break
        if not winning_board:
            losers.append(board)

    return winners, losers


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
            winning_boards, losing_boards = find_winners(boards)
            boards = losing_boards  # stop checking winning boards
            # Find the last board to win
            if len(losing_boards) == 0:
                print("found last board to win")
                winning_board = calculate_scores(winning_boards)
                break

    print(winning_boards)
    print(winning_board["score"] * number)
