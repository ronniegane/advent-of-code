"""
Counting orbits

essentially we are building a tree, calculating the depth of each node, and summing up the depth.

each node should have its children and a depth

we traverse down the tree calculating depth of each node, and then build up the total on the way back up
"""
from typing import List, Dict
from pathlib import Path


def sum_tree(node, orbit_map: Dict[str, List[str]], depth: int):
    # Add on the depth of this node
    sum = depth
    if node in orbit_map:  # This planet has satellites
        for child in orbit_map[node]:
            sum += sum_tree(child, orbit_map, depth+1)
    return sum


def build_map(orbits: List[str]):
    # Build up a map containing the planets and a list of each planet that orbits them
    orbit_map: Dict[str, List[str]] = {}
    for orbit in orbits:
        body, satellite = orbit.split(')')
        # Create entries if they don't exist
        if body not in orbit_map:
            orbit_map[body] = []
        orbit_map[body].append(satellite)
    return orbit_map


# Results:
# test = 42
# input =
path = (Path(__file__).parent.parent / ".././input").resolve()
fp = open(path, 'r')
orbits = [x.strip() for x in fp.readlines()]
fp.close()
orbit_map = build_map(orbits)
total = sum_tree('COM', orbit_map, 0)
print(total)
