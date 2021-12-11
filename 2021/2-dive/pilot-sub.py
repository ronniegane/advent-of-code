"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""

with open('input', 'r') as commands:
    x = 0
    y = 0
    for command in commands:
        direction, distance = command.split()
        if direction == 'forward':
            x += int(distance)
        elif direction == 'down':
            y += int(distance)
        elif direction == 'up':
            y -= int(distance)
        else:
            print('unknown command: ' + command)
    print(f'Final position: X: {x} , Y: {y}')
    print(x * y)
