WINDOW_SIZE = 3

count = 0

with open('input.txt') as f:
    window = []
    prev_sum = None

    for line in f:
        val = int(line.rstrip())

        window.append(val)
        window = window[-WINDOW_SIZE:]

        if len(window) < WINDOW_SIZE:
            continue

        curr_sum = sum(window)

        if prev_sum and curr_sum > prev_sum:
            count += 1

        prev_sum = curr_sum

print(count)