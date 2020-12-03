# Counting trees going right 3 and down 1
# As the pattern repeats, we wrap

fp = open('input', 'r')
pattern = [line.rstrip() for line in fp]
fp.close()
tree_count = 0
x = 0
for i, line in enumerate(pattern[1:]):  # Skip first row as we start there
    x += 3
    # print('(%d, %d) = %s' % (x, i, line[x % len(line)]))
    if line[x % len(line)] == '#':
        tree_count += 1

print(tree_count)
