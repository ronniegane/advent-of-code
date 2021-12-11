"""
gamma rate will always be the inverse of epsilon rate
"""


def binstring_to_decimal(binary_string):
    return int(f"0b{binary_string}", 2)


with open("input", "r") as report:
    """
    naive approach will be O(n * m)
    """
    oneCount = []
    # use first line to set width of oneCount array
    for column in report.readline().strip():
        # print(column)
        oneCount.append(column == "1")
    lineCount = 1

    for line in report:
        lineCount += 1
        column = 0
        for column, bit in enumerate(line):
            if bit == "1":
                oneCount[column] += 1

    # now have a count of the ones in each column
    gamma = ""
    epsilon = ""
    for count in oneCount:
        # are ties counted as a 1 or 0?
        if count >= lineCount / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")

    decimalGamma = binstring_to_decimal(gamma)
    decimalEpsilon = binstring_to_decimal(epsilon)
    print(f"decimal gamma: {decimalGamma}")
    print(f"decimal epsilon: {decimalEpsilon}")

    print(f'power consumption: {decimalGamma * decimalEpsilon}')
