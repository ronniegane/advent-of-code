with open('input', 'r') as fp:
    seen = {}
    for line in fp:
        num = int(line)
        # Check if we've seen its partner number before
        if (2020 - num) in seen:
            print ((2020 - num) * num)
            break
        else:
            # Build up the list of numbers we've seen
            seen[num] = True
