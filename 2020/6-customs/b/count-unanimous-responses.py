"""
count questions in each group where everyone answered
Build a hashmap then count all that appear as often as the number of lines
"""

from pathlib import Path


def count_unanimous(group: str):
    # Count of lines is count of '\n' character + 1, as no trailing '\n'
    answer_count = {'\n': 1}
    for answer in group:
        if answer not in answer_count:
            answer_count[answer] = 0
        answer_count[answer] += 1

    sum = 0
    for key, val in answer_count.items():
        if key != '\n':
            if val == answer_count['\n']:
                sum += 1

    # print(sum)
    return sum


path = (Path(__file__).parent / "./input").resolve()
fp = open(path, 'r')
groups = fp.read().strip().split('\n\n')
count = 0
for group in groups:
    count += count_unanimous(group)
print(count)
# test output should be 6
