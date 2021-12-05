horiz = 0
depth = 0

with open('input.txt') as f:
    for line in f:
        cmd, val = line.rstrip().split(' ')
        val = int(val)

        match cmd:
            case 'forward':
                horiz += val

            case 'down':
                depth += val

            case 'up':
                depth -= val

print(horiz * depth)