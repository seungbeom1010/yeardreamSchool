import itertools

n, m = map(int, input().split())

list_sample = [] 

for i in range(1, n+1):     # N까지의 숫자를 문자열 형태로 list에 추가
    list_sample.append(str(i))

result = list(itertools.product((list_sample), repeat=m)) # list_sample ** m 조합 

for j in result:
    print(*j)