"""
find the first number in the sequence which is NOT
a sum of two of the previous five numbers

Naive approach: recalculate each time

for x in array[5:]: # main loop
    for y in array[x-5:x]:
        for z in array[y+1:x]:
            if value(y) + value(z) = (x)
                return true / continue out to main loop
    # if we get here, then we have found a number that
    # cannot be made, which is our answer


Complexity of this solution:
loop in main code is O(n)
found_sum is O(k^2) where k is the size of the subarray, which = 5 in our case
or 25 in our main case but is still constant
so overall it is still O(n)

First guess for input is 35
"""
from pathlib import Path
from typing import List


def found_sum(sublist: List[int], target: int):
    # Returns True if we can make a sum from the provided list
    for j in range(0, len(sublist)):
        for k in range(j+1, len(sublist)):
            # if target can be reached by sum
            if (sublist[j] + sublist[k]) == target:
                return True
    return False


path = (Path(__file__).parent / "../input").resolve()
fp = open(path, 'r')
values = [int(x) for x in fp.readlines()]
fp.close()

lookback = 25 # How many pervious numbers to look at

for i in range(lookback, len(values)):
    if found_sum(values[i-lookback:i], values[i]) == False:
        print(values[i])
        break
