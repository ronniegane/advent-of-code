"""
Count the jolt gaps between each consecutive adapter

This should be possible just by sorting the list and counting up differences
"""

from pathlib import Path
from typing import Dict

# Test1: 7x 1-jolt, 5x 3-jolt differences
# Test2: 22x 1-jolt, 10x 3-jolt
# Input:
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
adapters = [int(x) for x in fp.readlines()]
fp.close()

adapters.append(0)  # Include the power outlet itself
adapters.sort()
adapters.append(adapters[-1] + 3)  # Include the device, 3 higher than highest

gaps: Dict[int, int] = {}
for i in range(len(adapters) - 1):
    gap = adapters[i+1] - adapters[i]
    if gap not in gaps:
        gaps[gap] = 0
    gaps[gap] += 1

print(gaps)
print(gaps[1] * gaps[3])
