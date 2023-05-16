def num_stairs(N):
    mod = 1000000000
    dp = [[0 for i in range(10)] for j in range(101)]
    for j in range(1, 10):
        dp[1][j] = 1
    for i in range(2, N+1):
        for j in range(1, 10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
    ans = 0
    for j in range(1, 10):
        ans = (ans + dp[N][j]) % mod
    return ans

if __name__ == "__main__":
    N = int(input().strip())
    print(num_stairs(N))
