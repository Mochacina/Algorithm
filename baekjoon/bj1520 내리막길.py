m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

dp = [[0]*n for _ in range(m)]
dp[0][0] = 1

cells = []
for i in range(m):
    for j in range(n):
        cells.append((board[i][j], i, j))

cells.sort(reverse=True)  # 높이 내림차순

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

for h, x, y in cells:
    if dp[x][y] == 0:
        continue
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < h:
                dp[nx][ny] += dp[x][y]

print(dp[m-1][n-1])

# m,n = map(int,input().split())
# l = [[*map(int,input().split())]for _ in range(m)]
# dp = [[-1]*n for _ in range(m)]
# di = [(0,1),(1,0),(0,-1),(-1,0)]

# def dfs(x,y):
#     if x==m-1 and y==n-1: return 1
    
#     if dp[x][y] != -1: return dp[x][y]
#     dp[x][y] = 0
    
#     for dx,dy in di:
#         nx,ny = x+dx,y+dy
#         if 0<=nx<m and 0<=ny<n:
#             if l[nx][ny] < l[x][y]:
#                 dp[x][y] += dfs(nx,ny)
    
#     return dp[x][y]
    
# print(dfs(0,0))



# for i in dp:
#     print(*i)


# M, N = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(M)]

# dp = [[-1] * N for _ in range(M)]

# dy = (-1, 1, 0, 0)
# dx = (0, 0, -1, 1)

# def solve(y, x):
#     if y == M-1 and x == N-1: # 종료 조건
#         return 1

#     if dp[y][x] != -1: # 메모이제이션
#         return dp[y][x]

#     dp[y][x] = 0
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]

#         if not (0 <= ny < M and 0 <= nx < N):
#             continue

#         if arr[ny][nx] < arr[y][x]:
#             dp[y][x] += solve(ny, nx)
#     return dp[y][x]

# print(solve(0, 0))

