
n = int(input())
powders = list(map(int, input().split())) 

result = [powders[0], powders[1]] 
sum = abs(sum(result)) # result 안 2개의 분말이 가지는 매운 정도

for i in range(n-1): # 순차적으로 분말 매움 수치 비교 
    for j in range(i+1, n):
        if abs(powders[i] + powders[j]) < sum: # result 안 기존 분말의 매운수치보다 0에 가까울 경우 
            sum = abs(powders[i] + powders[j])
            result[0] = powders[i]
            result[1] = powders[j]
        elif abs(powders[i] + powders[j]) == sum: # result 안 기존 분말의 매운수치랑 같을 경우 
            if abs(result[0]) + abs(result[1]) < abs(powders[i]) + abs(powders[j]):
                result[0] = powders[i]
                result[1] = powders[j]
                sum = abs(powders[i] + powders[j])
            else:
                pass
        else:
            pass

print(*result)
