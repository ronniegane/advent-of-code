"""
How many different bags can have a shiny gold bag inside them?

Sounds kind of like we need to build a directional graph of bags: bags are the nodes, "contains" are the edges

Assume there will be no cycles in the graph - that would lead to infinitely nested bags

Alternative: build up a map for each bag colour showing what it contains
Is that just a graph anyway?
have it 

How do we find the root of the tree?

Probably a better map is contained by, so we can go from shiny gold bag UP.
"""

from pathlib import Path
from typing import Dict, List, Set


def count_containers(bag: str, contained_by: Dict[str, List[str]], seen: Set[str]):
    # Recursively build a set of containers that contain the base bag
    seen.add(bag)
    for container in contained_by[bag]:
        if container not in seen:
            count_containers(container, contained_by, seen)
    return seen


# Test: 4 bags can contain shiny gold
# Input: 226
path = (Path(__file__).parent / '../test').resolve()
fp = open(path, 'r')

# parse rules
contained_by: Dict[str, List[str]] = {}
for line in fp.readlines():
    # X bags contain Y bag/s, Z bag/s.
    container, bagstring = line.strip('.\n').split(' bags contain ')

    # Ignore "no other bags", remove number of bags and "bag/s" word
    bags = [' '.join(x.split()[1:-1])
            for x in bagstring.split(', ') if x != 'no other bags']

    # Make sure top-level containers are still in the dict to keep things simple
    if container not in contained_by:
        contained_by[container] = []

    for bag in bags:
        if bag not in contained_by:
            contained_by[bag] = []
        contained_by[bag].append(container)

# Find set of containers that contain the base bag
set_of_bags = count_containers('shiny gold', contained_by, set())
set_of_bags.discard('shiny gold')  # Doesn't count itself
print(len(set_of_bags))

fp.close()
