import os

"""
This is much easier if we don't care about the order of the fish in the list,
just the count of each number
"""

with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "input")), "r"
) as input:
    fish_counts = {x: 0 for x in range(0, 9)}

    # Get initial fish count
    for fish in input.readline().strip().split(","):
        fishy_int = int(fish)
        fish_counts[fishy_int] = fish_counts[fishy_int] + 1

    initial_sum = 0
    for count in fish_counts.values():
        initial_sum += count

    print(f"initial fish count: {initial_sum}")
    print(fish_counts)

    # Age fish
    days_to_simulate = 256
    for day in range(1, days_to_simulate + 1):
        new_fish_counts = {x: 0 for x in range(0, 9)}
        for key, value in fish_counts.items():
            if key == 0:
                # Spawn a new fish
                new_fish_counts[8] = value
                new_fish_counts[6] += value
            elif key == 7:
                new_fish_counts[6] += value
            else:
                new_fish_counts[key - 1] = value
        fish_counts = new_fish_counts

    final_sum = 0
    for count in fish_counts.values():
        final_sum += count

    print(f"final fish count: {final_sum}")
    print(fish_counts)
