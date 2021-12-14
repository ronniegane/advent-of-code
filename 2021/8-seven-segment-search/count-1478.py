import os

"""
For part one, we only have to count how many times the digits 1, 4, 7 and 8 appear.
These are easily identifiable as they have a unique number of symbols(signals)
1 = two chars
4 = four chars
7 = three chars
8 = seven chars

So we can just grab the strings after the | separator and check for these lengths.
"""

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    special_digit_count = 0
    for line in input:
        output_digits = line.split("|")[1].split()
        # print(output_digits)
        for digit in output_digits:
            if len(digit) in [2, 4, 3, 7]:
                special_digit_count += 1

    print(special_digit_count)
