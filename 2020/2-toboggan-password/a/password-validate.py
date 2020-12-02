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
        # 1-3 a: abcde means between 1 and 3 appearances of 'a'
        rule, password = line.split(':')
        limits, char = rule.split(' ')
        min, max = limits.split('-')
        if isValid(char, int(min), int(max), password):
            count += 1
    print(count)
