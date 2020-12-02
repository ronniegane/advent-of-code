def isValid(char: str, min: int, max: int, password: str):
    count = 0
    valid = False
    for letter in password:
        if letter == char:
            count += 1
        if count > max:
            return False  # Break early
    return count >= min


# Parse the input file
with open('input', 'r') as fp:
    count = 0
    for line in fp:
        # 1-3 a: abcde means 'a' at position 1 XOR 'a' at position 3
        rule, password = line.split(': ')
        positions, char = rule.split(' ')
        first, second = [int(x) for x in positions.split('-')]
        if (password[first - 1] == char) != (password[second - 1] == char):
            count += 1
    print(count)
