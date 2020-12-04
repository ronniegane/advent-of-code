"""
Rules:
1. six-digit number
2. puzzle input gives range limit
3. At least one pair  of adjacent digits are the same
4. These matching digits are not part of a larger group, that is rule 3 is updated to
    TWO AND ONLY TWO 
5. Digits never decrease left to right

Rule 3/4 might be simpler to solve with regex but more interesting to do without

six-digit numbers means the range is at most 900,000
so brute force is probably possible
"""


def test_candidate(candidate: int):
    pair = False  # rule 3
    # Use integer division and modulo to get digits from right to left
    last_digit = candidate % 10
    candidate = candidate // 10
    streak = 1  # Run of the same number
    while candidate > 0:
        digit = candidate % 10

        if digit == last_digit:
            streak += 1  # the streak records how many times in a row we have seen this number
        else:
            if streak == 2:  # previous streak was only 2 digits long
                pair = True
            streak = 1  # reset count

        if digit > last_digit:
            # Break early if right digit less than left digit (rule 5)
            return False

        candidate = candidate // 10
        last_digit = digit

    if streak == 2:
        pair = True  # if the streak is in the two left-most numbers

    # If we get this far we passed rule 5, so only depends on rule 3/4
    return pair


def crack_password(min: int, max: int):
    possible_solutions = 0
    for candidate in range(min, max+1):
        if test_candidate(candidate):
            # Found a potential solution
            possible_solutions += 1
    print(possible_solutions)


crack_password(137683, 596253)
