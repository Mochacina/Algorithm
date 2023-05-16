n = int(input())
l = [0]*10000
for i in range(n):
    l[i] = int(input())
dp = [0]*10000
dp[0] = l[0]
dp[1] = l[0]+l[1]
dp[2] = max(dp[1],l[0]+l[2],l[1]+l[2])
for i in range(3, n): dp[i] = max(dp[i-3] + l[i-1] + l[i], dp[i-2] + l[i], dp[i-1])
print(max(dp))

    #dp[i-3] + l[i-1] + l[i]
    #dp[i-2] + l[i]
    #dp[i-1]2