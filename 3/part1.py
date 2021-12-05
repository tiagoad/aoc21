bit_counts = None
line_count = 0

with open('input.txt') as f:
    for line in f:
        num = list(map(int, list(line.rstrip())))

        if bit_counts is None:
            bit_counts = [0] * len(num)

        bit_counts = [a + b for a, b in zip(bit_counts, num)]

        line_count += 1

gamma = int(''.join(['1' if x >= (line_count / 2) else '0' for x in bit_counts]), 2)
epsilon = int(''.join(['1' if x <= (line_count / 2) else '0' for x in bit_counts]), 2)

print(gamma)
print(epsilon)
print(gamma * epsilon)