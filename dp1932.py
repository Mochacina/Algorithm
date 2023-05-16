n = int(input())
l = []
dp = [[0]*(n) for _ in range(n)]
for i in range(n):
    l.append(list(map(int,input().split())))
dp[0][0] = l[0][0]
if n>2:
    for i in range(1,n):
        for j in range(len(l[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + l[i][j]
            elif j == len(l[i])-1:
                dp[i][j] = dp[i-1][j-1] + l[i][j]
            else:
                dp[i][j] = max((dp[i-1][j] + l[i][j]),(dp[i-1][j-1] + l[i][j]))
print(max(dp[n-1]))