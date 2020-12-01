"""
For each number 'a' check if we've seen (2020 - a) yet
"""
def solve_double(nums: list[int]):
    seen = {}
    for a in nums:
        # Check if we've seen its partner number before
        if (2020 - a) in seen:
            print ((2020 - a) * a)
            break
        else:
            # Build up the list of numbers we've seen
            seen[a] = True

"""
With three numbers to get, we need to find
a pair (a,b) that has a matching single c that brings the total to 2020

Extending the logic from 1A slightly leads to an O(n^2) solution
"""
def solve_triple(nums: list[int]):
# really just using functions so I can break out of both loops
    seen = {}
    for i, a in enumerate(nums):
        for b in nums[i:]:
            if (2020 - a - b) in seen:
                return (a * b * (2020 - a - b))
        seen[a] = True
    return 0

with open('input', 'r') as fp:
    nums = [int(line) for line in fp]
    print (solve_triple(nums))
