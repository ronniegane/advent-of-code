with open('input', 'r') as fp:
    total = 0
    for line in fp:
        total += int(line) // 3 - 2
    print (total)
