import os

"""
This sounds like I want to build up a tree as we go
of bits, with the size of each subtree stored in the node
"""


class BitTree:
    def __init__(self):
        self.one = None
        self.zero = None
        self.count = 0


def binstring_to_decimal(binary_string):
    return int(f"0b{binary_string}", 2)


with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as report:
    bit_tree = BitTree()

    for line in report:
        current = bit_tree
        for char in line.strip():
            if char == "0":
                if current.zero == None:
                    current.zero = BitTree()
                current.zero.count = current.zero.count + 1
                current = current.zero
            elif char == "1":
                if current.one == None:
                    current.one = BitTree()
                current.one.count = current.one.count + 1
                current = current.one

    # Oxygen generator takes most common
    oxygen_rating = ""
    oxygen_tree = bit_tree
    while oxygen_tree.one != None or oxygen_tree.zero != None:  # Keep going til leaf
        if oxygen_tree.zero == None:
            oxygen_rating += "1"
            oxygen_tree = oxygen_tree.one
        elif oxygen_tree.one == None:
            oxygen_rating += "0"
            oxygen_tree = oxygen_tree.zero
        elif oxygen_tree.one.count >= oxygen_tree.zero.count:
            oxygen_rating += "1"
            oxygen_tree = oxygen_tree.one
        else:
            oxygen_rating += "0"
            oxygen_tree = oxygen_tree.zero

    print(f"oxygen rating: {oxygen_rating}")
    decimal_oxygen_rating = binstring_to_decimal(oxygen_rating)
    print(f"decimal oxygen rating: {decimal_oxygen_rating}")

    # CO2 scrubber takes least common
    co2_rating = ""
    co2_tree = bit_tree
    while co2_tree.one != None or co2_tree.zero != None:  # Keep going til leaf
        if co2_tree.zero == None:
            co2_rating += "1"
            co2_tree = co2_tree.one
        elif co2_tree.one == None:
            co2_rating += "0"
            co2_tree = co2_tree.zero
        elif co2_tree.one.count < co2_tree.zero.count:
            co2_rating += "1"
            co2_tree = co2_tree.one
        else:
            co2_rating += "0"
            co2_tree = co2_tree.zero

    print(f"co2 rating: {co2_rating}")
    decimal_co2_rating = binstring_to_decimal(co2_rating)
    print(f"decimal co2 rating: {decimal_co2_rating}")

    print(f"answer: {decimal_oxygen_rating * decimal_co2_rating}")
