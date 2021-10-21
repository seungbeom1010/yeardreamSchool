n = int(input())

num_list = []

for i in range(1, n + 1):
    num_list.append(str(i))

num_list = "".join(num_list)

print(num_list.find(str(n)) + 1)
