T = int(input())
len_A = int(input())
A_list1 = list(map(int, input().split()))
len_B = int(input())
B_list1 = list(map(int, input().split()))

A_sums = {}
for i in range(len_A):
    sub_sum = 0
    for j in range(i, len_A):
        sub_sum += A_list1[j]
        if sub_sum in A_sums:
            A_sums[sub_sum] += 1
        else:
            A_sums[sub_sum] = 1

result = 0
for i in range(len_B):
    B_sum = 0
    for j in range(i, len_B):
        B_sum += B_list1[j]
        A_sum = T - B_sum
        if A_sum in A_sums:
            result += A_sums[A_sum]

print(result)
