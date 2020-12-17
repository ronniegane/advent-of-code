"""
Once we find our target number, we can search through the list with a sliding window:
At each step:
- If we are below the target, include the next number to the right
- If we are above the target, remove the leftmost number
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

lookback = 25  # How many pervious numbers to look at
target = 0
for i in range(lookback, len(values)):
    if found_sum(values[i-lookback:i], values[i]) == False:
        target = values[i]
        break

print('target is %d' % target)
# For input, target is 27911108
# For test, target is 127
left = 0
right = 0
sum = values[0]
while right < 500 and sum != target:
    if sum < target:
        # Add the next value to our set
        right += 1
        sum += values[right]
        # print(values[left:right+1])
        # print('[%d, %d]: %d (%d)' % (left, right, sum, sum-target))
    elif sum > target:
        # Remove the leftmost value
        sum -= values[left]
        left += 1
        # print(values[left:right+1])
        # print('[%d, %d]: %d (%d)' % (left, right, sum, sum-target))

print('Window is [%d, %d]' % (left, right))
window = values[left:right+1]
# print(window)

# Find the minimum and maximum values
min_val = min(window)
max_val = max(window)
print('%d + %d = %d' % (min_val, max_val, max_val + min_val))
