import sys
import math

#60점 수정 필요

n, s = map(int, sys.stdin.readline().split())
goods = list(map(int, sys.stdin.readline().split()))

result = math.inf

if sum(goods) < s:
    print(0)

else:
    for i in range(n):
        sum_value = 0
        result = min(result, len(goods[i:]))
    
    print(result)