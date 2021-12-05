lines = []
bounds = (0, 0)

def rng(start, stop):
    return range(
        start, 
        stop + 1 if stop > start else stop - 1, 
        1 if stop > start else -1)

with open('input.txt') as f:
    for line in f:
        a, b = line.rstrip().split(' -> ')
        x1, y1 = [int(n) for n in a.split(',')]
        x2, y2 = [int(n) for n in b.split(',')]

        lines.append((x1, y1, x2, y2))
        bounds = (
            max(bounds[0], x1, x2),
            max(bounds[1], y1, y2)
        )

print(f'Bounds: {bounds}')
print(f'Lines: {len(lines)}')

counts = [[0] * (bounds[0] + 1) for i in range(bounds[1] + 1)]

for x1, y1, x2, y2 in lines:
    if x1 == x2:
        for i in rng(y1, y2):
            counts[i][x1] += 1

    elif y1 == y2:
        for i in rng(x1, x2):
            counts[y1][i] += 1

    else:
        for x, y in zip(rng(x1, x2), rng(y1, y2)):
            counts[y][x] += 1

count = 0
for l in counts:
    for v in l:
        if v > 1:
            count += 1

print(count)