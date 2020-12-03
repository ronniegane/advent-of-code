# Counting trees going right 3 and down 1
# As the pattern repeats, we wrap

from typing import List


def count_trees(patten: List[str], x_inc: int, y_inc: int):
    tree_count = 0
    x = 0
    y = 0
    width = len(pattern[0])
    while y < len(pattern)-1:
        x += x_inc
        y += y_inc
        # print('(%d, %d) = %s' % (x, y, pattern[y][x % width]))
        if pattern[y][x % width] == '#':
            tree_count += 1

    return tree_count


fp = open('input', 'r')
pattern = [line.rstrip() for line in fp]
fp.close()

slopes_to_check = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

total = 1
for slope in slopes_to_check:
    total *= count_trees(pattern, slope[0], slope[1])

print(total)
