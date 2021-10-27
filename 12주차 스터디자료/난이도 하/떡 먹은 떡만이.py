
M = []

for i in range(int(input())):
    M.append(list(map(int, input().split())))

dduck = [1, 0, 0]       # 떡 현재 위치

for i in range(len(M)):     # 떡 위치 이동
    if dduck[M[i][0] - 1] == 1:
        dduck[M[i][0] - 1] = 0
        dduck[M[i][1] - 1] = 1
    elif dduck[M[i][1] - 1] == 1:
        dduck[M[i][0] - 1] = 1
        dduck[M[i][1] - 1] = 0
    else:
        continue

print(dduck.index(1) + 1) # 현재 떡 위치 index 출력