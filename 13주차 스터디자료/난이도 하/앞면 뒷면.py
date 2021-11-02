import sys
n = int(sys.stdin.readline())

#80점 수정필요

cards = [0] * n

for i in range(n):
    for j in range(n):
        if (j + 1) % (i + 1) == 0 and cards[j] == 0:
            cards[j] = 1
        elif (j + 1) % (i + 1) == 0 and cards[j] == 1:
            cards[j] = 0

print(cards.count(1))