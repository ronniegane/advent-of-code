"""
Count the number of times that the number is larger
than the previous one.
"""

with open('input', 'r') as fp:
    # get first number
    last = int(fp.readline())
    increaseCount = 0
    for line in fp:
        current = int(line)
        if current > last:
            increaseCount += 1
        last = current
    print(increaseCount)
