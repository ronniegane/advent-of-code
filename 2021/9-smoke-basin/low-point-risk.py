import os

def pretty_print(matrix):
    print("\n".join(["\t".join(str(cell) for cell in row) for row in matrix]))


def print_bold(matrix, bold_cells):
    # highlight low points in red
    print("\n".join(["\t".join(
        f"\033[91m{str(cell)}\033[0m" if bold_cells[i][j] else str(cell) for j, cell in enumerate(row)
        ) for i, row in enumerate(matrix)]))


with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    risk_sum = 0
    # build the grid
    height_map = []
    possible_lowpoint = []
    for line in input:
        row = [int(x) for x in line.strip()]
        height_map.append(row)
        possible_lowpoint.append([True for x in row])

    # For iteration we only have to check down and right
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if i < len(height_map) - 1:
                if height_map[i + 1][j] >= height:
                    # We are lower than the south
                    possible_lowpoint[i + 1][j] = False
                else:
                    # We are taller than the south
                    possible_lowpoint[i][j] = False
            if j < len(row) - 1:
                if height_map[i][j + 1] >= height:
                    # We are lower than the east
                    possible_lowpoint[i][j + 1] = False
                else:
                    possible_lowpoint[i][j] = False

            # If after this check we are still at a lowpoint, add to the risk sum
            if possible_lowpoint[i][j]:
                risk = height + 1
                risk_sum += risk

    # pretty-print maps
    # pretty_print(height_map)
    # print("------------------------------")
    # pretty_print([[1 if x else 0 for x in row] for row in possible_lowpoint])
    # print("------------------------------")
    print_bold(height_map, possible_lowpoint)
    print("------------------------------")
    print(f"total risk: {risk_sum}")
