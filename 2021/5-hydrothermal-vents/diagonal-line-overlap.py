import os

"""
First approach:
Build up a map of points that have been covered
and increment the times this

Could use an NxN grid, or just a map so it's a bit faster than having to do an N^2 iteration at the end.
"""

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    vents = {}
    for line in input:
        # expected format is 0,9 -> 5,9
        start, end = line.strip().split(" -> ")
        x1, y1 = [int(z) for z in start.split(",")]
        x2, y2 = [int(z) for z in end.split(",")]

        # Build a map of vent locations with the count of lines crossing at each vent
        if x1 == x2 or y1 == y2:
            # could make this a bit more DRY
            if x1 == x2:
                if y1 <= y2:
                    for i in range(y1, y2 + 1):
                        if (x1, i) in vents:
                            vents[(x1, i)] = vents[(x1, i)] + 1
                        else:
                            vents[(x1, i)] = 1
                else:
                    for i in range(y2, y1 + 1):
                        if (x1, i) in vents:
                            vents[(x1, i)] = vents[(x1, i)] + 1
                        else:
                            vents[(x1, i)] = 1
            elif y1 == y2:
                if x1 <= x2:
                    for i in range(x1, x2 + 1):
                        if (i, y1) in vents:
                            vents[(i, y1)] = vents[(i, y1)] + 1
                        else:
                            vents[(i, y1)] = 1
                else:
                    for i in range(x2, x1 + 1):
                        if (i, y1) in vents:
                            vents[(i, y1)] = vents[(i, y1)] + 1
                        else:
                            vents[(i, y1)] = 1
        else:  # Have to consider diagonal lines for part 2
            # Diagonal lines will always be 45 degrees
            x_gradient = 1 if (x2 > x1) else -1
            y_gradient = 1 if (y2 > y1) else -1
            line_length = (x2 - x1) * x_gradient
            curr_x, curr_y = (x1, y1)
            for step in range(0, line_length + 1):
                if (curr_x, curr_y) in vents:
                    vents[(curr_x, curr_y)] = vents[(curr_x, curr_y)] + 1
                else:
                    vents[(curr_x, curr_y)] = 1
                curr_x = curr_x + x_gradient
                curr_y = curr_y + y_gradient

    overlap_count = 0
    for count in vents.values():
        if count > 1:
            overlap_count += 1

    print(overlap_count)
