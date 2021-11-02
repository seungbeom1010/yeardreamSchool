n_book = int(input())
books = [int(x) for x in input().split()]

sorted_books = []
count = 0

for i in range(1, n_book+1):
    if books.index(i) == i - 1:
        continue
    else:
        count += 1
        del books[books.index(i)]
        books.insert(i-1, i)

print(count)