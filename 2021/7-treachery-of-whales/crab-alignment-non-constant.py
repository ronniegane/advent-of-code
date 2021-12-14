import os

"""
Similar to previous problem
except now the fuel used to get from x to y is
1 + 2 + 3 + ... + n where n = abs(x-y)
This sum is equivalent to (n)(n+1)/2 or (n^2 + n)/2
ie
n   fuel
0   0
1   1
2   3
3   6
4   10
5   15

So this should only require a small change to the fuel calculation step
"""

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:

    crabs = [int(x) for x in input.readline().strip().split(",")]
    """
    Naive approach: check every number from min to max, and calculate
    complexity: N*K where K = (max - min)
    finding min and max is also O(N)
    """
    min_crab = min(crabs)
    max_crab = max(crabs)

    print(f"Minimum position: {min_crab}")
    print(f"Maximum position: {max_crab}")

    min_fuel = None
    min_fuel_position = 0
    for i in range(min_crab, max_crab + 1):
        fuel = 0
        for crab in crabs:
            distance = abs(crab - i)
            fuel += distance * (distance + 1) / 2
        print(f"Position {i} : Fuel required {fuel}")
        if min_fuel is None or min_fuel > fuel:
            min_fuel = fuel
            min_fuel_position = i

    print(f"Minimum fuel {min_fuel} units with alignment position {min_fuel_position}")
