def calc_fuel(mass : int):
    total = 0
    mass = mass // 3 - 2
    while mass > 0:
        total += mass
        mass = mass // 3 - 2
    return total

with open('input', 'r') as fp:
    total = 0
    for line in fp:
        total += calc_fuel(int(line))
    print (total)
