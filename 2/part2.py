horiz = 0
depth = 0
aim = 0

with open('input.txt') as f:
    for line in f:
        cmd, val = line.rstrip().split(' ')
        val = int(val)

        match cmd:
            case 'forward':
                horiz += val
                depth += aim * val

            case 'down':
                aim += val

            case 'up':
                aim -= val

print(horiz * depth)