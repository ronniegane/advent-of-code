"""
We want each bus to arrive at time T + i
where i is its index in the list of buses (including x)

The question indicates that the solution is going to be > 100000000000000 (10^14)
Brute-force solution is going to be terribly slow,
so we need to find an algorithm or a formulaic solution
"""

from pathlib import Path
import math

# Test1: first occurs at 1068781
# Test2: first occurs at 3417
# Test3: first occurs at 754018
# Test4: first occurs at 779210
# Test5: first occurs at 1261476
# Test6: first occurs at 1202161486
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
