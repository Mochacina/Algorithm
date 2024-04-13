n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
r = float('inf')
for start in range(3):
    dp = [[float('inf')]*3 for _ in range(n)]
    dp[0][start] = l[0][start]
    
    for i in range(1,n):
        for color in range(3):
            dp[i][color] = min(dp[i-1][(color+1)%3], 
                               dp[i-1][(color+2)%3]) + l[i][color]

    for color in range(3):
        if color != start:
            r = min(r, dp[n-1][color])

print(r)

# n = int(input())
# cost = [list(map(int, input().split())) for _ in range(n)]

# result = float('inf')

# # 첫 번째 집의 색을 고정하고 계산
# for first in range(3):
#     dp = [[float('inf')] * 3 for _ in range(n)]
#     dp[0][first] = cost[0][first]

#     for i in range(1, n):
#         for color in range(3):
#             dp[i][color] = min(dp[i-1][(color+1)%3], dp[i-1][(color+2)%3]) + cost[i][color]

#     # 마지막 집에서 첫 번째 집의 색과 다른 색만 고려
#     for color in range(3):
#         if color != first:
#             result = min(result, dp[n-1][color])

# print(result)