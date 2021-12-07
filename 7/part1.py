import statistics
import math

with open('input.txt') as f:
    for line in f:
        origposx = list(map(int, line.rstrip().split(',')))

optimal = statistics.median(origposx)
cost = int(sum(map(lambda x: abs(x - optimal), origposx)))

print(cost)