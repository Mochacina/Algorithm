n,m,k = map(int,input().split())
board = [[*input()]for _ in range(n)]
ps = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
        if "WB"[(i+j)%2] != board[i-1][j-1]: ps[i][j] += 1

ans = 9e9
for j in range(k, m+1):
    for i in range(k,n+1):
        cnt = ps[i][j] - ps[i-k][j] - ps[i][j-k] + ps[i-k][j-k]
        ans =  min(cnt, ans, k*k-cnt)

print(ans)

# for i in range(n-k):
#     for j in range(m-k):
#         total_changes = (
#             ps[i + k][j + k]
#             - ps[i][j + k]
#             - ps[i + k][j]
#             + ps[i][j]
#         )
#         ans = min(ans, total_changes, k * k - total_changes)

# print(ans)
    
# ans = 9e9
# kk = k*k

# for i in range(k-1, min(n,m)):
#     sum1 = -ps[i][i]
#     for j in range(i, i-k, -2):
#         sum1 += ps[i][j]
#         if 0 <= i-k and 0 <= j-k:
#             sum1 -= ps[i-k][j-k]
#     for j in range(i, i-k, -2): sum1 += ps[j][i]
#     sum2 = 0
#     for j in range(i-1, i-k, -2): sum2 += ps[i][j]
#     for j in range(i-1, i-k, -2): sum2 += ps[j][i]
#     print(sum1,sum2)
    
#     ans = min(kk-sum1, kk-sum2, sum1, sum2)

# print(ans)