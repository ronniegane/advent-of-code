"""
Finding the intersection that is the shortest total path along both wires

Could record in the map the number of steps each wire has taken.
When we find an intersection, sum up and record it

Can a wire ever cross over itself? If that is possible we need to handle it differently (keep the lowest step count)
Below code works on the assumption that wires never cross themselves.
"""
from pathlib import Path


# test1 distance 30
# test2 distance 610
# test3 distance 410


path = (Path(__file__).parent.parent / ".././input").resolve()
with open(path, 'r') as fp:
    crossovers = {}
    first_commands = fp.readline().split(',')
    grid = {}
    current_x = 0
    current_y = 0
    step_count = 0
    # Draw first circuit
    print('Drawing first circuit:')
    for command in first_commands:
        direction = command[0]
        distance = int(command[1:])
        # print('Current position is (%d, %d)' % (current_x, current_y))
        # print(command)
        if direction == 'L':
            for x in range(current_x-1, current_x - distance - 1, -1):
                step_count += 1
                grid["%d,%d" % (x, current_y)] = step_count
            current_x = current_x - distance
        elif direction == 'R':
            for x in range(current_x+1, current_x + distance + 1):
                step_count += 1
                grid["%d,%d" % (x, current_y)] = step_count
            current_x = current_x + distance
        elif direction == 'U':
            for y in range(current_y+1, current_y + distance + 1):
                step_count += 1
                grid["%d,%d" % (current_x, y)] = step_count
            current_y = current_y + distance
        elif direction == 'D':
            for y in range(current_y-1, current_y - distance - 1, -1):
                step_count += 1
                grid["%d,%d" % (current_x, y)] = step_count
            current_y = current_y - distance

    # Draw second circuit
    second_commands = fp.readline().split(',')
    current_x = 0
    current_y = 0
    min_dist = 10000000
    min_coords = [0, 0]
    step_count = 0

    print('\nDrawing second circuit:')
    # At each step check for overlaps and keep track of the closest overlap seen so far
    for command in second_commands:
        direction = command[0]
        distance = int(command[1:])
        # print('Current position is (%d, %d)' % (current_x, current_y))
        # print(command)
        if direction == 'L':
            for x in range(current_x-1, current_x - distance - 1, -1): # Start at x-1 so we don't write to the same map value twice
                step_count += 1
                if "%d,%d" % (x, current_y) in grid:
                    dist_to_home = step_count + grid["%d,%d" % (x, current_y)]
                    if dist_to_home < min_dist:
                        min_dist = dist_to_home
                        min_coords = [x, current_y]
            current_x = current_x - distance
        elif direction == 'R':
            for x in range(current_x+1, current_x + distance + 1):
                step_count += 1
                if "%d,%d" % (x, current_y) in grid:
                    dist_to_home = step_count + grid["%d,%d" % (x, current_y)]
                    if dist_to_home < min_dist:
                        min_dist = dist_to_home
                        min_coords = [x, current_y]
            current_x = current_x + distance
        elif direction == 'U':
            for y in range(current_y+1, current_y + distance + 1):
                step_count += 1
                if "%d,%d" % (current_x, y) in grid:
                    dist_to_home = step_count + grid["%d,%d" % (current_x, y)]
                    if dist_to_home < min_dist:
                        min_dist = dist_to_home
                        min_coords = [current_x, y]
            current_y = current_y + distance
        elif direction == 'D':
            for y in range(current_y-1, current_y - distance - 1, -1):
                step_count += 1
                if "%d,%d" % (current_x, y) in grid:
                    dist_to_home = step_count + grid["%d,%d" % (current_x, y)]
                    if dist_to_home < min_dist:
                        min_dist = dist_to_home
                        min_coords = [current_x, y]
            current_y = current_y - distance
        # pretty_print(grid)

    print('Crossover at (%d, %d) distance of %d' %
          (min_coords[0], min_coords[1], min_dist))
    # How to ignore the (0,0) crossover?
