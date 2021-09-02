"""
Seating Simulator

This bears simularities to Conway's Game of Life.

Rules are:
- All seats start empty (L)
Each round:
1. If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
2. If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
3. Otherwise, the seat's state does not change.

We notice two things:
1. Since all seats start empty, the second state will always be all seats full.
2. Seats that remain full after the third state will always stay full, because they _never_ have four occupied neighbours even if all seats are full. This may mean that we can remove them from the list of seats to check.

Naive approach: build a 2D array, and iterate through it each time.
Flip a flag if any changes are made.

Part Two introduces different considerations for "adjacent" seats - now it is the first seat in that direction.
Worst case, if there are no seats between this seat and the edge of the grid, we check
(a + b + 2 * sqrt(a^2 + b^2)) locations for a single seat on an a x b grid

"""

from pathlib import Path
from copy import deepcopy


def count_neighbours(x, y, grid):
    count = 0
    left = max(x-1, 0)
    right = min(x+2, len(grid[0]))
    top = max(y-1, 0)
    bottom = min(y+2, len(grid))
    for i in range(top, bottom):
        for j in range(left, right):
            # Ignore the square itself
            if (y != i or x != j) and grid[i][j] == '#':
                count += 1
    return count


def grid_print(grid):
    for line in grid:
        print(''.join(line))


# Test: 37 occupied seats once stable
# Input: 2289 occupied seats once stable
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
grid = [[x for x in y.strip()] for y in fp.readlines()]
# grid_print(grid)
fp.close()
# Loop until stable
unstable = True
rounds = 0
while unstable:
    # print('-------------')
    next_grid = deepcopy(grid)
    unstable = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                # floor; skip
                continue
            occupied_count = count_neighbours(x, y, grid)
            if grid[y][x] == 'L' and occupied_count == 0:
                # Empty seat becomes occupied
                unstable = True
                next_grid[y][x] = '#'
            elif grid[y][x] == '#' and occupied_count >= 4:
                # Occupied seat becomes empty
                unstable = True
                next_grid[y][x] = 'L'
    grid = next_grid
    rounds += 1
    # grid_print(grid)

print('Stable in %d rounds' % rounds)
# Count occupied seats
count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            count += 1

print(count)
