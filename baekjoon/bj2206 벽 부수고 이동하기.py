# from collections import deque
# n,m = map(int, input().split())
# l = [list(map(int, input())) for _ in range(n)]
# di = [(0,1),(0,-1),(1,0),(-1,0)]
# v = [[0]*m for _ in range(n)]
# nodes = deque([(0,0)])
# v[0][0] = 1

# def bfs(nodes, i):
#     nodes_n = deque()
#     while nodes:
#         x,y = nodes.popleft()
#         cnt = v[x][y]
#         for dx,dy in di:
#             nx, ny = x+dx, y+dy
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not v[nx][ny] or v[nx][ny] > cnt+1:
#                     if l[nx][ny] and i==0:
#                         nodes_n.append((nx,ny))
#                         v[nx][ny] = cnt+1
#                     elif not l[nx][ny]:
#                         nodes.append((nx,ny))
#                         v[nx][ny] = cnt+1
#     return nodes_n

# for i in range(2):
#     nodes = bfs(nodes, i)
    
# print(v[n-1][m-1] if v[n-1][m-1] else -1)
              
# for i in v:
#     print(*i)


# from collections import deque

# n, m = map(int, input().split())
# l = [list(map(int, input())) for _ in range(n)]
# di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# v = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# queue = deque([(0, 0, 0)])  # (x, y, 벽 부순 횟수)
# v[0][0][0] = 1  # 시작 위치 초기화

# while queue:
#     x, y, broke = queue.popleft()
#     cnt = v[x][y][broke]
#     if x == n-1 and y == m-1:
#         print(cnt)
#         break

#     for dx, dy in di:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < m:
#             if l[nx][ny] == 1 and broke == 0 and v[nx][ny][1] == 0:
#                 # 벽을 만나고 아직 벽을 부수지 않았다면, 벽을 부수고 진행
#                 v[nx][ny][1] = cnt + 1
#                 queue.append((nx, ny, True))
#             elif l[nx][ny] == 0 and v[nx][ny][broke] == 0:
#                 # 벽이 없고, 아직 방문하지 않은 경우
#                 v[nx][ny][broke] = cnt + 1
#                 queue.append((nx, ny, broke))

# else:
#     print(-1)  # (n, m) 위치에 도달할 수 없는 경우

from collections import deque
n,m = map(int, input().split())
l = [list(map(int, input())) for _ in range(n)]
di = [(0,1),(0,-1),(1,0),(-1,0)]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][0] = 1

q = deque([(0,0,0)])
while q:
    x,y,z = q.popleft()
    if x == n-1 and y == m-1:
        print(v[x][y][z])
        break
    for dx,dy in di:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if l[nx][ny] == 1 and z == 0:
                v[nx][ny][1] = v[x][y][z] + 1
                q.append((nx,ny,1))
            elif l[nx][ny] == 0 and not v[nx][ny][z]:
                v[nx][ny][z] = v[x][y][z] + 1
                q.append((nx,ny,z))
else:print(-1)