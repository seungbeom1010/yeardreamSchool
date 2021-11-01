def solution(change, coins, n_coins):
    dp = [0] * (change + 1)     # dp index 값 = 해당 index를 만드는 경우의 수
    dp[0] = 1
    
    for i in range(n_coins):
        for j in range(coins[i], change + 1):
            dp[j] += dp[j - coins[i]]
    
    return dp[change]

n_coins = int(input())
coins = list(map(int, input().split()))
change = int(input())

print(solution(change, coins, n_coins))