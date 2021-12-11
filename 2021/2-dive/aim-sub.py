"""
down X increases the aim by X units.
up X decreases the aim by X units.

forward X does two things:
- It increases your horizontal position by X units.
- It increases your depth by your aim multiplied by X.
"""

with open('input', 'r') as commands:
    x = 0
    y = 0
    aim = 0
    for command in commands:
        direction, distance = command.split()
        if direction == 'forward':
            x += int(distance)
            y += aim * int(distance)
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
        else:
            print('unknown command: ' + command)
    print(f'Final position: X: {x} , Y: {y}')
    print(x * y)
