import sys
a = [0]*1024
b = [0]*1024
dp = [[], []]
p = False
q = False
input = sys.stdin.readline
k, n, m = map(int, input().split())
for i in range(1, k + 1):
    a[i], b[i] = map(int, input().split())
dp[0] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1] = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
p = 1
q = 0
for i in range(1, k + 1):
    p, q = q, p
    for x in range(0, n + 1):
        for y in range(0, m + 1):
            dp[q][x][y] = dp[p][x][y]
            if x:  
                dp[q][x][y] = max(dp[q][x][y], dp[p][x - 1][y] + a[i])
            if y: 
                dp[q][x][y] = max(dp[q][x][y], dp[p][x][y - 1] + b[i])
print(dp[q][n][m])