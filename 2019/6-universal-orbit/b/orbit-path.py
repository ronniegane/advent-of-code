"""
Building a path from one orbit to another

Using the tree from before, the answer is basically
- Find the common ancestor of SAN and YOU - call it X
- Add the distance (X -> SAN) to the distance (X -> YOU)

The latter could be written as
depth(SAN) + depth(YOU) - 2*depth(X)
"""
from typing import List, Dict
from pathlib import Path


class Node:
    """Represents a planet or other space object.
    children are objects orbiting this one
    depth is the number of orbits between this and COM
    """

    def __init__(self, name):
        self.name: str = name
        self.depth: int = 0
        self.children: List[str] = []

    def add_child(self, child):
        self.children.append(child)


def calc_depths(node: str, orbit_map: Dict[str, Node], depth: int):
    """Calculates and records the depth of each node against its entry in the map.
    Doesn't sum the depths, just modifies the map
    """
    if node in orbit_map:  # This planet has satellites
        for child in orbit_map[node].children:
            calc_depths(child, orbit_map, depth+1)
    else:
        # leaf node, need to add to map
        orbit_map[node] = Node(node)
    orbit_map[node].depth = depth


def nearest_common_ancestor(alpha: str, beta: str, orbit_map: Dict[str, Node]):
    # TODO implement
    return 'COM'


def build_map(orbits: List[str]):
    # Build up a map containing the planets
    orbit_map: Dict[str, Node] = {}
    for orbit in orbits:
        body, satellite = orbit.split(')')
        # Create entries if they don't exist
        if body not in orbit_map:
            orbit_map[body] = Node(body)
        orbit_map[body].add_child(satellite)
    return orbit_map


# Expected:
# test = 4
# input =
path = (Path(__file__).parent.parent / ".././test-b").resolve()
fp = open(path, 'r')
orbits = [x.strip() for x in fp.readlines()]
fp.close()

# Build the tree
orbit_map = build_map(orbits)
calc_depths('COM', orbit_map, 0)

# Find nearest common ancestor
ancestor = nearest_common_ancestor('SAN', 'YOU', orbit_map)

# Calculate distance
distance = orbit_map['SAN'].depth + \
    orbit_map['YOU'].depth - 2 * orbit_map[ancestor].depth
print(distance)
