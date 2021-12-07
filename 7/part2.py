import statistics
import math

with open('input.txt') as f:
    for line in f:
        origposx = list(map(int, line.rstrip().split(',')))


minx = min(origposx)
maxx = max(origposx)

# get triangular numbers
triang = []
for n in range(0, (maxx - minx) + 1):
    triang.append((triang[-1] if triang else 0) + n)

# find optimal cost
mincost = None
for x in range(minx, maxx + 1):
    cost = 0
    for crabx in origposx:
        cost += triang[abs(crabx - x)]
    if (not mincost) or mincost > cost:
        mincost = cost

print(mincost)
