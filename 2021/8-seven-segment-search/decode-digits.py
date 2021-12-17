import os

"""
For part two, we actually have to decode the digits

for clarity, let's label the physical segments of the display as
TUVXYZ
 TTTT
U    V
U    V
 WWWW
X    Y
X    Y
 ZZZZ

With that, we can build a map of numbers:
"""
segments_to_numbers = {
    "TUVXYZ": 0,
    "VY": 1,
    "TVWXZ": 2,
    "TVWYZ": 3,
    "UVWY": 4,
    "TUWYZ": 5,
    "TUWXYZ": 6,
    "TVY": 7,
    "TUVWXYZ": 8,
    "TUVWYZ": 9,
}
"""
From here we can see some ways to deduce wires:
0. as before, 1 4 7 8 are immediate identifiable
1. The wire that is on for 7 but off for 1 is T
2. The wires on for 4 but off for 1 are UW
4. 9 is the only digit to be a superset of 4
5. The wires on for 9 but off for 4 are TZ
6. The wire on for 8 but off for 9 is X

Signal lengths:
2: 1
3: 7
4: 4
5: 2 3 5
6: 0 6 9
7: 8

Out of curiousity, the number of times each segment is used in a 0-9 display is
T 8
U 6
V 8
W 7
X 4
Y 9
Z 7

So we can identify U, X and Y just by how often a given letter/signal appears in the left-hand-side of the input.
And since we know T from above, we can deduce V, then the only ones left are W and Z, which are the only unknowns 7 appearances.

And we can get Z from combining some knowns
"""

# Return a map from signal combination to digit
def find_translation(rosetta_stone):
    signal_digit_mapping = {}
    digit_signal_mapping = {}

    # print(rosetta_stone)
    # map the easy numbers
    unknowns = []
    for signal in rosetta_stone:
        if len(signal) == 2:
            signal_digit_mapping[signal] = 1
            digit_signal_mapping[1] = signal
        elif len(signal) == 3:
            signal_digit_mapping[signal] = 7
            digit_signal_mapping[7] = signal
        elif len(signal) == 4:
            signal_digit_mapping[signal] = 4
            digit_signal_mapping[4] = signal
        elif len(signal) == 7:
            signal_digit_mapping[signal] = 8
            digit_signal_mapping[8] = signal
        else:
            unknowns.append(signal)

    # print(digit_signal_mapping)
    # Identify some signal wires and which segments they light up
    # by how often they are used
    signal_segment_mapping = {}
    signal_counts = {}
    for signal in rosetta_stone:
        for char in signal:
            if char not in signal_counts:
                signal_counts[char] = 1
            else:
                signal_counts[char] = signal_counts[char] + 1

    # print(signal_counts)

    for char in digit_signal_mapping[7]:
        if char not in digit_signal_mapping[1]:
            signal_segment_mapping[char] = "T"

    for char, count in signal_counts.items():
        if count == 6:
            signal_segment_mapping[char] = "U"
        elif count == 4:
            signal_segment_mapping[char] = "X"
        elif count == 9:
            signal_segment_mapping[char] = "Y"
        elif count == 8:
            if char not in signal_segment_mapping:
                # This is V, not T
                signal_segment_mapping[char] = "V"

    # print(signal_segment_mapping)

    # Unknown signals at this point only W and Z
    for char in digit_signal_mapping[4]:
        if char not in signal_segment_mapping:
            # must be W as we know UVY already
            signal_segment_mapping[char] = "W"

    for char in digit_signal_mapping[8]:
        if char not in signal_segment_mapping:
            # must be Z as the only unknown
            signal_segment_mapping[char] = "Z"

    # print(signal_segment_mapping)

    # build the whole thing
    signalset_to_segmentset_mapping = {
        signalset: "".join(
            sorted([signal_segment_mapping[signal] for signal in signalset])
        )
        for signalset in rosetta_stone
    }
    # print(signalset_to_segmentset_mapping)

    signalset_to_digit_mapping = {
        signalset: segments_to_numbers[segmentset]
        for (signalset, segmentset) in signalset_to_segmentset_mapping.items()
    }

    # print(signalset_to_digit_mapping)
    return signalset_to_digit_mapping


with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    sum = 0
    for line in input:
        digit_sets = line.strip().split("|")
        rosetta_stone = [
            "".join(sorted(x)) for x in digit_sets[0].split()
        ]  # Sort letters in each string alphabetically

        # Find mapping from signal sets to digits
        translation_map = find_translation(rosetta_stone)

        output_digits = ["".join(sorted(x)) for x in digit_sets[1].split()]
        output_number = int("".join([str(translation_map[k]) for k in output_digits]))
        sum += output_number

    print(f"total sum: {sum}")
