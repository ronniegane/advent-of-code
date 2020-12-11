"""
How many permutations are possible with:
- increasing numbers
- gap of 3 or less between each numbers
the ends are always fixed, so it's just permutations of the middle N numbers

Naive implementation would be recursive:
1. Start at one end
2. At each point where you have a choice of adapters (gap between 1 and 3), branch and calculate perms from that point on
3. Pass count up to the root

Worst case, if all adapters are 1 jolt apart, each one has 3 alternative children (ignoring the last ones)
so branching factor 3
O(3^n)

Another option - calculate how many neighbours each adapter has?


What does this look like mathematically?
P(N) = P(N+1) + P(N+2) + P(N+3)
P(N) = (P(N+2)+P(N+3)+P(N+4)) + P(N+2) + P(N+3)

but this only holds if each P(x) exists

It does imply that we could build things up in reverse from the device end
Or we could do it going forward from the wall end, because it is symmetrical problem if we look at it from the other direction

Q(N) = Q(N-1) + Q(N-2) + Q(N-3)
Q = permutations between here and the wall
P = permutations between here and the device
Q is mentally easier as it's left-to-right

eg if we have
  0 1 4 5 6 7 8
so 0 and 8 are mandatory (wall and device)

The permutations are
0 1 4 5 6 7 8
0 1 4 5 6 8
0 1 4 5 7 8
0 1 4 5 8
0 1 4 6 7 8
0 1 4 6 8
0 1 4 7 8

7 total perms

we can fill in with Q(X) = 0 if X not in the set
then apply Q(N) = Q(N-1) + Q(N-2) + Q(N-3)

n 0 1 (2) (3) 4 5 6 7 8
Q 1 1  0   0  1 1 2 4 7

check with test1
[0] 1 4 5 6 7 10 11 12 15 16 19 [22]
expand
[0] 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 [22]
 1  1 0 0 1 1 2 4 0 0  4  4  8  0  0  8  8  0  0  8   8 

This solution is O(n log(n)) for the sort
and O(n) for the permutation calculation
"""

from pathlib import Path

# Test1: 8 permutations
# Test2: 19208 permutations
# Input:
path = (Path(__file__).parent / '../input').resolve()
fp = open(path, 'r')
adapters = [int(x) for x in fp.readlines()]
fp.close()

adapters.append(0)  # Include wall socket
adapters.sort()
adapters.append(adapters[-1] + 3)  # Include device

perms = {0: 1}  # Permutations possible stopping at each point
for adapter in adapters[1:]:
    a = perms.get(adapter-1, 0)
    b = perms.get(adapter-2, 0)
    c = perms.get(adapter-3, 0)
    perms[adapter] = a+b+c

print(perms[adapters[-1]])  # Perms at the device
