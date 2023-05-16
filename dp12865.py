a,b = map(int,input().split())
l = [[0,0]]
dp = [[0] * (b+1) for i in range(a+1)]
for i in range(a):
    l.append(list(map(int,input().split())))
for i in range(1,a+1):
    for j in range(1,b+1):
        if j<l[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-l[i][0]]+l[i][1] , dp[i-1][j])
print(dp[a][b])