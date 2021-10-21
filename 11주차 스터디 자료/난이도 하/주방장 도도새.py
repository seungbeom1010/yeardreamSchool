count, work_time = map(int, input().split())
order_list = [int(x) for x in input().split()]

sum = 0
result = 0

for i in range(count):
    sum += order_list[i]
    if sum <= work_time:
        result += 1

print(result)