from collections import deque

r,c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[-1]*c for _ in range(r)]
node_l, node_r = [], []
ice_l, ice_r = [], []
days = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == 'L' and not node_l:
            node_l.append((i,j))
            board[i][j] = '.'
        else:
            node_r.append((i,j))
            board[i][j] = '.'
            
def dfs(nodes, n):
    q = deque(nodes)
    while q:
        x,y = q.popleft()
        if visited[x][y] == -1: visited[x][y] = days*2+n
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1:
                if board[nx][ny] == '.' and visited[nx][ny] == -1:
                    visited[nx][ny] = days*2+n
                    q.appendleft((nx,ny))
                elif board[nx][ny] == '.' and visited[nx][ny]%2+1 == n:
                    return True
                elif board[nx][ny] == 'X':
                    if n == 0: ice_l.append((nx,ny))
                    else: ice_r.append((nx,ny))
    return 0

dfs(node_l, 0)
dfs(node_r, 1)
for i in board:
    print(*i)
for i in visited:
    print(*i)

# while days < 10:
#     if dfs(node_l, 0): break
#     if dfs(node_r, 1): break
#     days += 1
#     for x,y in ice_l:board[x][y] = '.'
#     for x,y in ice_r:board[x][y] = '.'
#     node_l = ice_l
#     node_r = ice_r
#     ice_l = []
#     ice_r = []
#     print(days)
#     for i in board:
#         print(*i)
#     print(visited)
    
# print(days)

# from collections import deque

# r, c = map(int, input().split())
# board = [list(input()) for _ in range(r)]
# visited = [[-1] * c for _ in range(r)]
# swans = []  # 백조의 위치 저장

# for i in range(r):
#     for j in range(c):
#         if board[i][j] == 'L':
#             swans.append((i, j))
#             board[i][j] = '.'  # 백조 위치도 물로 처리

# # BFS 함수 정의
# def bfs(start_nodes, mark):
#     q = deque(start_nodes)
#     next_ice = []
#     while q:
#         x, y = q.popleft()
#         for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1:
#                 if board[nx][ny] == '.':
#                     visited[nx][ny] = mark
#                     q.append((nx, ny))
#                 elif board[nx][ny] == 'X':
#                     visited[nx][ny] = mark
#                     next_ice.append((nx, ny))
#     return next_ice

# ice_l = bfs([swans[0]], 0)  # 첫 번째 백조 위치에서 시작
# ice_r = bfs([swans[1]], 1)  # 두 번째 백조 위치에서 시작

# days = 0
# while True:
#     new_ice_l = []
#     new_ice_r = []
#     for x, y in ice_l:
#         board[x][y] = '.'
#         new_ice_l.extend(bfs([(x, y)], 0))
#     for x, y in ice_r:
#         board[x][y] = '.'
#         new_ice_r.extend(bfs([(x, y)], 1))
#     ice_l = new_ice_l
#     ice_r = new_ice_r
#     days += 1

#     # 만남 체크
#     for x, y in ice_l:
#         if visited[x][y] == 1:
#             print(days)
#             exit(0)

#     for x, y in ice_r:
#         if visited[x][y] == 0:
#             print(days)
#             exit(0)
