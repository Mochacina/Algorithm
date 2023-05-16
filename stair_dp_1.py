def num_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 9
    mod = 1000000000
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * 10 - dp[i - 2]) % mod
    return dp[n]

n = int(input().strip())
print(num_stairs(n) % 1000000000)


