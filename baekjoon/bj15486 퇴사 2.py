import sys
input = sys.stdin.readline
n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
dp = [0]*(n+1)
for i in range(n):
    a,b = l[i]
    dp[i+1] = max(dp[i], dp[i+1])
    if i+a <= n: dp[i+a] = max(dp[i+a], dp[i]+b)
print(max(dp))