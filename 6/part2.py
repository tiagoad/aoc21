MAX_TIMER = 8
DAYS = 256

def tick(counts):
    new = [0] * len(counts)

    for i in range(MAX_TIMER, -1, -1):
        if i == 0:
            new[6] += counts[i]
            new[8] = counts[i]

        else:
            new[i-1] = counts[i]

    return new

def main():
    with open('input.txt') as f:
        fish = list(map(int, f.readline().rstrip().split(',')))

    # turn list of fish timers to count of
    # fish per timer value.
    counts = [0] * (MAX_TIMER + 1)
    for v in fish:
        counts[v] += 1

    for day in range(DAYS):
        counts = tick(counts)

    print('Final count:', sum(counts))

if __name__ == '__main__':
    main()
