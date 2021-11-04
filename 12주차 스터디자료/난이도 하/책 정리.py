from bisect import bisect_left

n = int(input())
book = list(map(int, input().split()))

dp = [0]
for i in book:
    if dp[-1] < i:
        dp.append(i)

    else:
        dp[bisect_left(dp, i)] = i


print(n - (len(dp) - 1))