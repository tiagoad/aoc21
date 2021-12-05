count = 0

with open('input.txt') as f:
    prev = None
    
    for line in f:
        val = int(line.rstrip())

        if prev and (val > prev):
            count += 1

        prev = val

print(count)