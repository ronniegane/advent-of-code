"""
Find the value in the accumulator just before we hit a loop
"""
from pathlib import Path

path = (Path(__file__).parent / "../test").resolve()
fp = open(path, 'r')
# Instructions [operation, value, order visited]
instructions = []
for line in fp.readlines():
    command = line.split()
    instructions.append([command[0], int(command[1]), 0])
fp.close()
