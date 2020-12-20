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
import math

# Test: should take bus 59 waiting 5 minutes  = 295
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
# First line is the earliest time _we_ can leave
time = int(fp.readline())
# Second line is bus IDs, ignore the "x" buses
buses = [int(x) for x in fp.readline().split(',') if x != 'x']
fp.close()

print(buses)

best_wait = math.inf  # Positive infinity
best_bus = 0
for bus_id in buses:
    arrival = (time // bus_id) * bus_id
    if arrival < time:  # allow for special case where bus arrives exactly on time
        arrival = arrival + bus_id

    wait = arrival - time
    # Probably could just have a formula for this
    if wait < best_wait:
        best_wait = wait
        best_bus = bus_id

print('Bus ID: %d Wait: %d = %d' % (best_bus, best_wait, best_bus * best_wait))
