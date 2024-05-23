# # n=10
# # 9876543210
# # n=11
# # 89876543210
# # 10123456789
# # n=12
# # 789876543210
# # 989876543210
# # 898765432101
# # 210123456789
# # 101234567898

# dp = [set()for _ in range(100)]
# dp[10].add("9876543210")
# print(dp)
# for i in range(11,30):
#     temp = set()
#     for j in dp[i-1]:
#         start = int(j[0])
#         end = int(j[-1])
#         if 1 < start < 9:
#             temp.add(str(start+1)+j)
#             temp.add(str(start-1)+j)
#         elif start == 9:
#             temp.add(str(start-1)+j)
#         else:
#             temp.add(str(start+1)+j)
#         if 0 < end < 9:
#             temp.add(j+str(end+1))
#             temp.add(j+str(end-1))
#         if end == 9:
#             temp.add(j+str(end-1))
#         else:
#             temp.add(j+str(end+1))
#     dp[i] = temp

# print(dp)
# for i in dp[10:41]:
#     print(len(i))


# dp = [[[0]*(1<<10) for _ in range(10)] for _ in range(101)]

# def num_of_stairs(N):
#     for i in range(1,10):
#         dp[1][i][1<<i] = 1
#     for i in range(2, N+1):
#         for j in range(10):
#             for bit in range(1024):
#                 if j == 0:
#                     dp[i][j][bit | (1 << j)] += dp[i-1][j+1][bit]
#                 elif j == 9:
#                     dp[i][j][bit | (1 << j)] += dp[i-1][j-1][bit]
#                 else:
#                     dp[i][j][bit | (1 << j)] += dp[i-1][j-1][bit] + dp[i-1][j+1][bit]

# num_of_stairs(N:=int(input().strip()))
# print(sum([dp[N][i][1023] for i in range(10)]) % 1000000000)

# dp = [[[[0]*2 for _ in range(2)] for _ in range(10)] for _ in range(101)]

# def num_of_stairs(N):
#     for i in range(1,10):
#         dp[1][i][i==9][i==0] = 1
#     for i in range(2, N+1):
#         for j in range(10):
#             for mx in range(2):
#                 for mn in range(2):
#                     if j == 0:
#                         dp[i][j][mx][1] += dp[i-1][j+1][mx][mn]
#                     elif j == 9:
#                         dp[i][j][1][mn] += dp[i-1][j-1][mx][mn]
#                     else:
#                         dp[i][j][mx][mn] += dp[i-1][j-1][mx][mn] + dp[i-1][j+1][mx][mn]

# num_of_stairs(N:=int(input().strip()))
# print(sum([dp[N][i][1][1] for i in range(10)]) % 1000000000)

N=int(input())
dp = [[[0]*4 for _ in range(10)]for _ in range(101)]

for i in range(1,10):
    dp[1][i][(i==9)*2] = 1
for i in range(2, N+1):
    for j in range(10):
        for bit in range(4):
            if j == 0:
                dp[i][j][bit|1] += dp[i-1][j+1][bit]
            elif j == 9:
                dp[i][j][bit|2] += dp[i-1][j-1][bit]
            else:
                dp[i][j][bit] += dp[i-1][j-1][bit] + dp[i-1][j+1][bit]

print(sum([dp[N][i][3] for i in range(10)]) % 1000000000)