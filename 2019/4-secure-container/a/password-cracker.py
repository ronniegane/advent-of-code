"""
Rules:
1. six-digit number
2. puzzle input gives range limit
3. At least one pair of adjacent digits are the same
4. Digits never decrease left to right

six-digit numbers means the range is at most 900,000
so brute force is probably possible
"""


def test_candidate(candidate: int):
    adjacents = False
    # Use integer division and modulo to get digits from right to left
    last_digit = candidate % 10
    candidate = candidate // 10
    while candidate > 0:
        digit = candidate % 10

        if digit == last_digit:
            adjacents = True  # Neighbouring pair found, passed rule 3
        if digit > last_digit:
            return False  # Break early if right digit less than left digit

        candidate = candidate // 10
        last_digit = digit
    # If we get this far we passed rule 4, so only depends on rule 3
    return adjacents


def crack_password(min: int, max: int):
    possible_solutions = 0
    for candidate in range(min, max+1):
        if test_candidate(candidate):
            # Found a potential solution
            possible_solutions += 1
    print(possible_solutions)


crack_password(137683, 596253)
