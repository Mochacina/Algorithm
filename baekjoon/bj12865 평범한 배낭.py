# a,b = map(int,input().split())
# dp = [[0] * (b+1) for i in range(a+1)]
# l = [[0,0]]+[[*map(int,input().split())] for _ in range(a)]
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if j<l[i][0]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-l[i][0]]+l[i][1] , dp[i-1][j])
# print(dp[a][b])


n,k = map(int,input().split())
items = [[0,0]]
for _ in range(n):
    w,v = map(int,input().split())
    items.append([w,v])
dp = [[0]*(k+1)for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        weight, value = items[i][0], items[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-weight] + value
            )
print(dp[n][k])


# ¼ôÄÚµù
# N,K,*l=map(int,open(0).read().split())
# d=-~K*[0]
# while l:
#  w,v,*l=l
#  for i in range(K,w-1,-1):d[i]=max(d[i],d[i-w]+v)
# print(d[K])