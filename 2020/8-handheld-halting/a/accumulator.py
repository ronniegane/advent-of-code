"""
Find the value in the accumulator just before we hit a loop
"""
from pathlib import Path

path = (Path(__file__).parent / "../input").resolve()
fp = open(path, 'r')
# Instructions [operation, value, order visited]
instructions = []
for line in fp.readlines():
    command = line.split()
    instructions.append([command[0], int(command[1]), 0])
fp.close()
accumulator = 0
index = 0
step = 1
# Keep going if we have not seen this instruction before
while instructions[index][2] == 0:
    # Record the order in which we reached instructions (may be useful later, idk)
    instructions[index][2] = step
    operation = instructions[index][0]
    if operation == 'nop':
        index += 1  # Just move on
    elif operation == 'acc':
        accumulator += instructions[index][1]
        index += 1
    elif operation == 'jmp':
        index += instructions[index][1]
print(accumulator)
