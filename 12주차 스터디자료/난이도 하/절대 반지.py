N = input()

Ring_List = []

for i in range(int(input())):
    Ring_List.append(list(map(str, input().split())))

count = 0

for j in Ring_List: # 절대 반지 문자열에 별명이 포함되어있으면 count + 1
    if N in "".join(j+j):
        count += 1

print(count)