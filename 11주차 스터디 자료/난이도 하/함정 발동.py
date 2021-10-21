
A_list = []
B_list = []

for i in range(8):
    n = list(map(str, input()))
    
    if len(A_list) <= len(B_list):
        A_list.append(n)
    else:
        B_list.append(n)

result = 0

for A in A_list:
    for i in range(0, 8, 2):
        if A[i] == 'H':
            result += 1

for B in B_list:
    for i in range(1, 8, 2):
        if B[i] == 'H':
            result += 1


print(result)
