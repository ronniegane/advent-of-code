"""
Assume that L and R can only be increments of 90 degrees so we only ever move North, South, East or West

We use a coordinate system where N and E are positive, and start at 0,0
"""


from pathlib import Path

# Test: should end up east 17, south 8 (17, -8) so manhattan distance is 25
path = (Path(__file__).parent / '../test').resolve()
fp = open(path, 'r')
# Format of each line is first character is direction, rest is value
movements = [[x[0], int(x[1:])] for x in fp.readlines()]
fp.close()

print(movements)
