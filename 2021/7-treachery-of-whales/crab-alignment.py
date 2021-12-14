import os

"""
In mathematical terms
for a set of numbers x1, x2, ...xn
find a number y such that
sum(abs(x-y)) is minimized.

Conjecture: this will be a number that has even amounts of numbers to the left and right.
Not sure how to prove/disprove

Conjecture: it will be close to the average number
counterexample: 0 0 0 0 100, average is 20, which gives 4x20 + 80 = 160, NOT the most efficient which would be y=0
Maybe close to the median?

Will sorting help?
Note: if you sort the numbers, ie sorted input is
0,1,1,2,2,2,4,7,14,16
Then run from both ends
0 increasing by 1
16 decreasing by 1
at each step the fuel cost goes up by K where K is the number of numbers < current X
find when both hit the same number

Is this the sort of thing that will have multiple local minima, or just one global minimum?
My instinct is that it's only a single minimum, but I don't know how to prove it.
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
            fuel += abs(crab - i)
        print(f"Position {i} : Fuel required {fuel}")
        if min_fuel is None or min_fuel > fuel:
            min_fuel = fuel
            min_fuel_position = i

    print(f"Minimum fuel {min_fuel} units with alignment position {min_fuel_position}")
