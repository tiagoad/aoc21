GRID_SIZE = 5

def check_won(marks):
    for i in range(0, GRID_SIZE):
        line = marks[GRID_SIZE*i:GRID_SIZE*i+GRID_SIZE]
        col = [marks[j] for j in range(i, len(marks), GRID_SIZE)]

        if all(line) or all(col):
            return True

    return False

def find_loser(numbers, cards):
    remaining = [(i, card, [False] * len(card)) for i, card in enumerate(cards)]

    for n in numbers:
        print('DREW', n, '\n')

        for ci, card, marks in remaining:
            for cni, cn in enumerate(card):
                if cn == n:
                    marks[cni] = True

        for ci, card, marks in remaining:
            # print card
            for j, m in enumerate(marks):
                print('X' if m else '_', end=' ')
                if j % GRID_SIZE == GRID_SIZE - 1:
                    print()
            print('\n')

        remaining = [(i, c, m) for i, c, m in remaining if not check_won(m)]

        if not remaining:
            return card, marks, n


if __name__ == '__main__':
    numbers = None
    cards = []

    with open('input.txt') as f:
        numbers = [int(n) for n in f.readline().rstrip().split(',')]

        for line in f:
            if len(line) == 1:
                cards.append([])

            cards[-1] += [int(n) for n in line.rstrip().split()]


    card, marks, number = find_loser(numbers, cards)
    score = 0
    for n, mark in zip(card, marks):
        if not mark:
            score += n

    print('SCORE:', score)
    print('DRAW: ', number)
    final_score = score * number

    print(final_score)
