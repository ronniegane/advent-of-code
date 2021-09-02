"""
Apply the bitmask to each command following it

could separate out the 1s and 0s from the Xs and apply two masks:
an OR with the 1 mask (0 at all other positions)
an AND with the 0 mask (1 at all other positions)

Recording values in memory: just use a dict?

"""
from pathlib import Path

# Test: should result in sum of 165
# Input: currently guessing 375776035880555 which is too high
path = (Path(__file__).parent / '../test2').resolve()
with open(path, 'r') as fp:
    mask = ''
    one_mask = 0b0
    zero_mask = 0b0
    memory = {}
    for line in fp:
        line = line.strip()
        if line.startswith('mask'):
            # Change the mask
            mask = line.split(' = ')[1]
            # Split the mask into two: one mask for setting to 0
            # and one mask for setting to 1
            for i in range(0, len(mask)):
                if mask[-i-1] == '0':
                    zero_mask += 2**i
                elif mask[-i-1] == '1':
                    one_mask += 2**i
            zero_mask = (2**len(mask) - 1) - zero_mask  # invert the zero mask
            print('0b'+mask)
            print(bin(one_mask))
            print(bin(zero_mask))
        elif line.startswith('mem'):
            mem, val = line.split(' =')
            val = int(val)
            print('original: ', bin(val))
            val = val & zero_mask
            print('after zero mask: ', bin(val))
            val = val | one_mask
            print('after one mask: ', bin(val))
            index = int(mem[4:-1])  # format mem[1234]
            memory[index] = val
            # print('put value %d at index %d' % (val, index))

    total = 0
    for v in memory.values():
        total += v
    print(total)
