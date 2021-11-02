import itertools

n, m = map(int, input().split())

list_sample = [] 

for i in range(1, n+1):
    list_sample.append(str(i))

result = list(itertools.combinations(list_sample, m)) 

for i in result:
    print(*i)