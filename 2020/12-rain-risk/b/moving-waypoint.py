"""
This time, all the instructions except for F move the waypoint, not the ship
Assume that L and R can only be increments of 90 degrees

We use a coordinate system where N and E are positive, and start at 0,0

The waypoint stays relative to the ship
F x means move the ship to the waypoint and repeat x times
eg if waypoint is at (2, 3) relative to the ship and we move F 10
we go 20 east and 30 north

We have to keep track of both the waypoint and the ship position because the final
answer is the ship's position relative to its starting point.
"""


from pathlib import Path


def move(x, y, direction, distance):
    # Move the object and return the new position
    if direction == 'E':
        x += distance
    elif direction == 'W':
        x -= distance
    elif direction == 'N':
        y += distance
    elif direction == 'S':
        y -= distance
    return x, y


# Test: should end up east 214, south 72 (214, 72) so manhattan distance is 286
# Input: ends up (-9828, 32245) and waypoint (-84, 45), manhattan distance 42073
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
# Format of each line is first character is direction, rest is value
movements = [[x[0], int(x[1:])] for x in fp.readlines()]
fp.close()

# Starting positions
ship_east = 0
ship_north = 0
waypoint_east = 10
waypoint_north = 1

for movement in movements:
    direction = movement[0]
    value = movement[1]
    # print(movement)
    if direction == 'R' or direction == 'L':
        """ Rotate the waypoint clockwise around the ship
        For each 90deg rotation:
        x = y
        y = -x

        eg waypoint (3, 4) rotates to:
        90 (4, -3)
        180 (-3, -4)
        270 (-4, 3)
        360 (3, 4)

        we could use the number of rotations mod 4 so we don't do unnecessary work
        or just learn the 3 cases:

        right 90 = left 270 = x -> y, y -> -x
        right 180 = left 180 = x -> -x, y -> -y
        right 270 = right 90 = x -> -y, y -> x
        (right 360 no change)
        """
        turn = value % 360 # Any number of full turns don't matter

        if direction == 'L':
            # A left turn is the mirror of a right turn
            turn = 360 - turn

        if turn == 90:
            waypoint_east, waypoint_north = waypoint_north, -1 * waypoint_east
        elif turn == 180:
            waypoint_east, waypoint_north = -1 * waypoint_east, -1 * waypoint_north
        elif turn == 270:
            waypoint_east, waypoint_north = -1 * waypoint_north, waypoint_east
        # Otherwise 0 or 360 so no change
    elif direction == 'F':
        # Move ship east X times waypoint east, and north X times waypoint north
        ship_east, ship_north = move(
            ship_east, ship_north, 'E', value * waypoint_east)
        ship_east, ship_north = move(
            ship_east, ship_north, 'N', value * waypoint_north)
    else:
        # Move waypoint in a cardinal direction
        waypoint_east, waypoint_north = move(
            waypoint_east, waypoint_north, direction, value)

    # print('ship (%d, %d), waypoint (%d, %d)' % (ship_east, ship_north, waypoint_east, waypoint_north))

print('Manhattan distance: %d' % (abs(ship_east) + abs(ship_north)))
