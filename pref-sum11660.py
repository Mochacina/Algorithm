import sys
input = sys.stdin.readline
a, b = map(int,input().split())
l = [list(map(int,input().split()))for _ in range(a)]
dp = [[0]*(a+1) for _ in range(a+1)]
for i in range(1,a+1):
    for j in range(1,a+1):
        dp[i][j] = l[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
for _ in range(b):
    x1,y1,x2,y2 = map(int,input().split())
    print(dp[x1-1][y1-1] + dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1])