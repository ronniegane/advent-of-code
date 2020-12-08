"""
Change exactly one jmp to nop or nop to jmp

Find the loop, it has to be one of the instructions within the infinite loop
Is this a candidate for backtracking search?
Depth-first search and branch our code when deciding to switch a nop or jmp
"""
from pathlib import Path
from typing import List
from copy import deepcopy


class Instruction:
    operation: str
    value: int
    visited: bool

    def __init__(self, operation, value):
        self.operation = operation
        self.value = value
        self.visited = False

    def __repr__(self) -> str:
        return "%s : %d : %r" % (self.operation, self.value, self.visited)

    def __str__(self) -> str:
        return "%s : %d : %r" % (self.operation, self.value, self.visited)


def proceed(instructions: List[Instruction], index: int, accumulator: int):
    # Carry out the instructions and return failure or success
    # Reset the point we branched at and start from there
    instructions[index].visited = False
    while index < len(instructions) and instructions[index].visited is False:
        operation = instructions[index].operation
        instructions[index].visited = True
        if operation == 'nop':
            index += 1  # Just move on
        elif operation == 'acc':
            accumulator += instructions[index].value
            index += 1
        elif operation == 'jmp':
            index += instructions[index].value
    # If we get here we either found a loop or finished the program (in the latter case index is 1 past the end)
    return index == len(instructions), accumulator


def search(instructions: List[Instruction]):
    accumulator = 0
    index = 0
    # Start the program, and branch whenever we find a 'nop' or 'jmp'
    while index < len(instructions):
        operation = instructions[index].operation
        instructions[index].visited = True
        if operation == 'nop':
            # Try swapping, if that reaches bottom then we need to switch this operation
            instructions[index].operation = 'jmp'
            # Need to copy instructions by value here
            success, result = proceed(
                deepcopy(instructions), index, accumulator)
            # Otherwise, proceed as normal
            if success:
                return result
            instructions[index].operation = 'nop'
            index += 1  # Just move on
        elif operation == 'jmp':
            # Try swapping, if that reaches bottom then we need to switch this operation
            instructions[index].operation = 'nop'
            # Need to copy instructions by value here
            success, result = proceed(
                deepcopy(instructions), index, accumulator)
            if success:
                return result
            instructions[index].operation = 'jmp'
            # Otherwise, proceed as normal
            index += instructions[index].value
        elif operation == 'acc':
            accumulator += instructions[index].value
            index += 1


path = (Path(__file__).parent / "../input").resolve()
fp = open(path, 'r')
# Instructions [operation, value, order visited]
instructions: List[Instruction] = []
for line in fp.readlines():
    command = line.split()
    instructions.append(Instruction(command[0], int(command[1])))
fp.close()
print(search(instructions))
