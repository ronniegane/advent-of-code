"""
How many bags total does a shiny gold bag have inside it?

We can build a map of the type, and count, of bags inside each kind of bag.
Then we can recursively build up a count of the children of this bag
Effectively just counting nodes in a tree
"""

from pathlib import Path
from typing import Dict, List, Set


class Rule:
    type: str
    amount: int

    def __init__(self, amount, type) -> None:
        self.amount = amount
        self.type = type


def count_children(bag: str, contains: Dict[str, List[Rule]]):
    count = 0
    for child in contains[bag]:
        count += child.amount
        count += child.amount * count_children(child.type, contains)
    return count


# Test1: 32 bags inside one shiny gold bag
# Test2: 126 bags
# Input: 226
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')

# parse rules
contains: Dict[str, List[Rule]] = {}
for line in fp.readlines():
    # X bags contain Y bag/s, Z bag/s.
    container, bagstring = line.strip('.\n').split(' bags contain ')

    # Ignore "no other bags", remove number of bags and "bag/s" word
    bags: List[Rule] = []
    for rulestring in bagstring.split(', '):
        if rulestring != "no other bags":
            ruleparts = rulestring.split()
            name = ' '.join(ruleparts[1:-1])
            amount = int(ruleparts[0])
            bags.append(Rule(amount, name))

    if container not in contains:
        contains[container] = []

    for bag in bags:
        if bag.type not in contains:  # Make sure bottom-level bags are included
            contains[bag.type] = []
        contains[container].append(bag)

count = count_children('shiny gold', contains)
print(count)

fp.close()
