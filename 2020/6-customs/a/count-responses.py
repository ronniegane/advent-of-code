"""
count questions in each group with at least one answer
essential is just "how many unique letters are in each set"

Luckily, python can turn strings directly into sets
"""

from pathlib import Path

path = (Path(__file__).parent / "./input").resolve()
fp = open(path, 'r')
groups = fp.read().split('\n\n')
count = 0
for group in groups:
    uniques = set(group)
    uniques.discard('\n')
    count += len(uniques)
print(count)
