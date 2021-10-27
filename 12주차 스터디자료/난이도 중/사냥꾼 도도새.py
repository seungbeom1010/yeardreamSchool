n = int(input())
spider = list(map(int, input().split()))

count = 0

for i in spider:
    bullet = i
    if bullet - 1 not in spider[spider.index(i)+1:]:
        count += 1

print(count)