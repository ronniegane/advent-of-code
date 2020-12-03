# Do we know the maximum size of the grid beforehand?
# Does python allow a dynamically sized 2D array? That would make things easier.

# First idea: create the grid and fill in first wire
# Draw second wire and check every step for an overlap
# Keep track of running minimum

# Second idea: convert directions to a series of nodes
# eg R8 U5 L5 D3 becomes (0,0) (8,0) (8,5) (3,5) (3,2)
# Then check for crossover with each step in the second one
# Would be O(n^2) as you check the whole list of the first wire
# for each edge in the second wire

# test1 distance 6
# test2 distance 159
# test3 distance 135

with open('test1', 'r') as fp:
    first_commands = fp.readline().split(',')
    grid = [[0]]
    current_x = 0
    current_y = 0
    # Grid limits
    right_edge = 0
    top_edge = 0
    # Draw first circuit
    for command in first_commands:
        direction = command[0]
        distance = int(command[1:])
        print('Current position is (%d, %d)' % (current_x, current_y))
        print(grid)
        print(command)
        if direction == 'L':
            for x in range(current_x-distance, current_x):
                grid[x][current_y] = 1
            current_x = current_x - distance
        elif direction == 'R':
            for x in range(current_x, current_x + distance + 1):
                # Expand grid if necessary
                if x > right_edge:
                    grid.append([0 for y in grid[0]])
                    right_edge += 1
                grid[x][current_y] = 1
            current_x = current_x + distance
        elif direction == 'U':
            for y in range(current_y, current_y + distance + 1):
                print('y is %d' % y)
                print('current_x is %d' % current_x)
                # Expand grid if necessary
                if y > top_edge:
                    for col in grid:
                        col.append(0)
                    top_edge += 1
                grid[current_x][y] = 1
            current_y = current_y + distance
        elif direction == 'D':
            for y in range(current_y - distance, current_y):
                grid[current_x][y] = 1
            current_y = current_y - distance

    # Draw second circuit
    second_commands = fp.readline().split(',')
    current_x = 0
    current_y = 0
    min_dist = 10000000
    min_coords = [0, 0]

    # At each step check for overlaps and keep track of the closest overlap seen so far
    for command in second_commands:
        direction = command[0]
        distance = int(command[1:])
        if direction == 'L':
            for x in range(current_x-distance, current_x):
                if grid[x][current_y] == 1:
                    distance = x + current_y
                    if distance < min_dist:
                        min_dist = distance
                        min_coords = [x, current_y]
            current_x = current_x - distance
        elif direction == 'R':
            for x in range(current_x, current_x + distance + 1):
                # Expand grid if necessary
                if x > right_edge:
                    grid.append([0 for y in grid[0]])
                    right_edge += 1
                if grid[x][current_y] == 1:
                    distance = x + current_y
                    if distance < min_dist:
                        min_dist = distance
                        min_coords = [x, current_y]
            current_x = current_x + distance
        elif direction == 'U':
            for y in range(current_y, current_y + distance + 1):
                # Expand grid if necessary
                if y > top_edge:
                    for col in grid:
                        col.append(0)
                    top_edge += 1
                if grid[current_x][y] == 1:
                    distance = current_x + y
                    if distance < min_dist:
                        min_dist = distance
                        min_coords = [current_x, y]
            current_y = current_y + distance
        elif direction == 'D':
            for y in range(current_y - distance, current_y):
                if grid[current_x][y] == 1:
                    distance = current_x + y
                    if distance < min_dist:
                        min_dist = distance
                        min_coords = [current_x, y]
            current_y = current_y - distance

    print('Crossover at (%d, %d) distance of %d' %
          (min_coords[0], min_coords[1], min_dist))
    # How to ignore the (0,0) crossover?
