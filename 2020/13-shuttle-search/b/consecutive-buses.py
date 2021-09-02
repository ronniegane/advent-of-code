"""
We want each bus to arrive at time T + i
where i is its index in the list of buses (including x)

The question indicates that the solution is going to be > 100000000000000 (10^14)
Brute-force solution is going to be terribly slow,
so we need to find an algorithm or a formulaic solution

Our search space is limited to numbers that are multiples of the bus that arrives at T+0 (assuming there is one)
in our input, there is such a bus, so we can work with this assumption
call that bus id X
that would still leave us with 10^14 / X values to check so we need more reduction than that.

for the next bus (Y), say it is arriving at T+1
arrives at a time M so that M % X = 1 and M % Y = 0
or more specifically, M = T + 1
but we could use the M % X = 1 rule to reduce search space

for the next bus (Z), arriving at T + 4
arrives at a time N so that N % X = 4 and N % Z = 0

Is there a relation here to the modulus between the ids?
As in, can we relate this to Y % X and Z % X ?

Looking at the visualised table in the question for ideas.
It looks kind of like we're effectively lining up slots in a rotating combination lock
Where each disk has a certain number of slots

If the lowest common multiple of all the numbers is K
then if we think about a disk of circumference K, all the disks representing each bus have evenly spaced slots

All the buses will arrive at the same time at LCM
How do you find the LCM of more than two numbers? Just repeated application?

And then, after the LCM, how do you find the situation where each slot is offset just right?


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
