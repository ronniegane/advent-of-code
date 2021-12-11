from collections import deque
"""
Using a three-measurement sliding window
is the sum of the current window > sum of the previous?
"""

with open('input', 'r') as fp:
    # get first window
    window = deque()

    a = int(fp.readline())
    b = int(fp.readline())
    c = int(fp.readline())

    # windowSum = a + b + c

    """
    Really all this needs to do is to compare line N with line N-3
    as lines N-1 and N-2 will be in both windows.
    """

    window.append(a)
    window.append(b)
    window.append(c)

    increaseCount = 0

    for line in fp:
        last = window.popleft()
        current = int(line)
        if current > last:
            increaseCount += 1
        window.append(current)
    print(increaseCount)
