"""
We want each bus to arrive at time T + i
where i is its index in the list of buses (including x)

Brute-force solution is going to be terribly slow,
so we need to find an algorithm or a formulaic solution
"""

from pathlib import Path
import math

# Test: first occurs at 1068781
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
# First line is the earliest time _we_ can leave
time = int(fp.readline())
# Second line is bus IDs, "x" buses are ignored but still affect list positions
buses = {}
offsets = {}
for i, x in enumerate(fp.readline().strip().split(',')):
    if x != 'x':
        # Active bus
        buses[int(x)] = i
        offsets[i] = int(x)

fp.close()

print(buses)
print(offsets)
