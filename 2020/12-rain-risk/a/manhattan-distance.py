"""
Assume that L and R can only be increments of 90 degrees so we only ever move North, South, East or West

We use a coordinate system where N and E are positive, and start at 0,0
"""


from pathlib import Path


def move(x, y, direction, distance):
    # Move the ship and return the new position
    if direction == 'E':
        x += distance
    elif direction == 'W':
        x -= distance
    elif direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    return x, y


# Test: should end up east 17, south 8 (17, -8) so manhattan distance is 25
# Input: ends up west 13, north 407 (-13, 407) so manhattan distance is 420
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
# Format of each line is first character is direction, rest is value
movements = [[x[0], int(x[1:])] for x in fp.readlines()]
fp.close()

east = 0
north = 0
headings = ['E', 'S', 'W', 'N']
current_heading = 'E'
for movement in movements:
    direction = movement[0]
    value = movement[1]
    print(movement)
    if direction == 'R':
        # Rotate degrees clockwise
        shift = value // 90
        index = (headings.index(current_heading) + shift) % len(headings)
        current_heading = headings[index]
    elif direction == 'L':
        # Rotate degrees anticlockwise
        shift = value // 90
        index = (headings.index(current_heading) - shift) % len(headings)
        current_heading = headings[index]
    elif direction == 'F':
        # Forward
        east, north = move(east, north, current_heading, value)
    else:
        east, north = move(east, north, direction, value)

    print('(%d, %d), heading %s' % (east, north, current_heading))

print('Manhattan distance: %d' % (abs(east) + abs(north)))
