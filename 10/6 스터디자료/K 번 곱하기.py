a, b = map(int, input().split())

sum = 0
for i in range(1, a+1): # 1부터 a번까지 자연수
    sum += i ** b # 각 자연수를 b승 한뒤 sum 값에 더하기

print(sum % 1000000009)
