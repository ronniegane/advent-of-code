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


def loop(master: List[int], goal: int):
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = master[:]  # Copy by value
            program[1] = noun
            program[2] = verb
            program = calculate(program)

            # Check
            if program[0] == goal:
                return noun, verb
    print('FAILED')
    return 0, 0


# Find the parameters at position 1 and 2 that will result in an output with 19690720 at position 0
# 100 possibilites for each = 10k combinations for brute force
with open('input', 'r') as fp:
    program = [int(x) for x in fp.readline().split(',')]
    noun, verb = loop(program, 19690720)
    print(noun, verb)
