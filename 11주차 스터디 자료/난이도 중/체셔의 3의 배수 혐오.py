import itertools

len_n = int(input())
n_list = [int(x) for x in input().split()]

all_n = list(itertools.permutations(n_list))

result = []

for n in all_n:
    temp = []
    for i in range(len_n - 1):
        temp.append((n[i] + n[i + 1])%3)
    
    if 0 not in temp:
        result.append(n)

if len(result) == 0:
    print(-1)
else:
    print( *result[0])
    