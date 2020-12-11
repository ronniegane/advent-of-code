"""
How many permutations are possible with:
- increasing numbers
- gap of 3 or less between each numbers
the ends are always fixed, so it's just permutations of the middle N numbers

Naive implementation would be recursive:
1. Start at one end
2. At each point where you have a choice of adapters (gap between 1 and 3), branch and calculate perms from that point on
3. Pass count up to the root

Worst case, if all adapters are 1 jolt apart, each one has 3 alternative children (ignoring the last ones)
so branching factor 3
O(3^n)
"""

from pathlib import Path

# Test1: 8 permutations
# Test2: 19208 permutations
# Input:
path = (Path(__file__).parent / '../test1').resolve()
fp = open(path, 'r')
adapters = [int(x) for x in fp.readlines()]
fp.close()

adapters.sort()
