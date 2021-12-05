GRID_SIZE = 5

def check_won(marks):
    for i in range(0, GRID_SIZE):
        line = marks[GRID_SIZE*i:GRID_SIZE*i+GRID_SIZE]
        col = [marks[j] for j in range(0, len(marks) - 1, GRID_SIZE)]

        if all(line) or all(col):
            return True

def find_winner(numbers, cards):
    card_marks = [[False] * len(c) for c in cards]

    for n in numbers:
        for card, marks in zip(cards, card_marks):
            for cni, cn in enumerate(card):
                if cn == n:
                    marks[cni] = True

            if check_won(marks):
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


    card, marks, number = find_winner(numbers, cards)
    score = 0
    for n, mark in zip(card, marks):
        if not mark:
            score += n
    final_score = score * number

    print(final_score)

