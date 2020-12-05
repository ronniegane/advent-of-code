# 1 = read next [a b c]. Put lookup(a) + lookup(b) at position c
# 2 = read next [a b c]. Put lookup(a) * lookup(b) at position c
# 99 = halt

from typing import List


def calculate(program: List[int]):
    command = program[0]
    startIndex = 0
    while command != 99:
        a, b, c = program[startIndex+1: startIndex+4]
        if command == 1:
            # Add
            program[c] = program[a] + program[b]
        elif command == 2:
            # Multiply
            program[c] = program[a] * program[b]
        else:
            print('ERROR')
            break
        startIndex += 4
        command = program[startIndex]
    return program
