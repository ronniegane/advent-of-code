"""
This should have an analytical solution
Each bus arrives at x, 2x, .... nx

For each bus, its latest arrival BEFORE time y is
(y // x) * x
using integer division
so its earliest arrival after time y is
(y // x) * x + x
we can just find these times and get the earliest
"""

from pathlib import Path

# Test: should take bus 59 waiting 5 minutes  = 295
path = (Path(__file__).parent / '../test').resolve()
fp = open(path, 'r')
# First line is the earliest time _we_ can leave
time = int(fp.readline())
# Second line is bus IDs, ignore the "x" buses
buses = [int(x) for x in fp.readline().split(',') if x != 'x']
fp.close()

print(buses)
