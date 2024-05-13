from collections import deque

n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
di = [(1,0),(-1,0),(0,1),(0,-1)]
v = []
shark_size, shark_exp = 2,0
total_times = 0

q = deque()
for x in range(n):
    for y in range(n):
        if l[x][y] == 9:
            q.append([x,y])
            l[x][y] = 0

def bfs(q):
    hunt_l = []
    time = 1
    # 잡아먹을 대상이 없고 다음 방문할 공간이 있으면 계속 돌아감
    while not hunt_l and q:
        next_node = deque()
        while q:
            x,y = q.popleft()
            for dx,dy in di:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n and l[nx][ny] <= shark_size:
                    # 잡아먹을 수 있는 물고기 있는 경우 무조건 먼저 잡아먹음
                    if l[nx][ny] and l[nx][ny] < shark_size:
                        hunt_l.append([nx,ny])
                        v[nx][ny] = time
                    # 잡아먹을 수 있는 물고기 없는 경우, 방문하지 않은 빈 공간 이동
                    elif not hunt_l and (not l[nx][ny] or l[nx][ny] == shark_size) and not v[nx][ny]:
                        next_node.append([nx,ny])
                        v[nx][ny] = time
        time += 1
        q = next_node
    if hunt_l:
        # 위에 있는놈 왼쪽에 있는놈 우선 잡아먹음
        hunt_l.sort()
        return hunt_l[0], time-1
    else:
        return [], 0

while 1:
    v = [[0]*n for _ in range(n)]
    v[q[0][0]][q[0][1]] = 1
    hunt, time = bfs(q)
    if not hunt:
        break
    x,y = hunt
    q = deque([[x,y]])
    l[x][y] = 0
    shark_exp += 1
    total_times += time
    if shark_exp == shark_size:
        shark_size += 1
        shark_exp = 0

print(total_times)

# from collections import deque

# n = int(input())
# l = [[*map(int, input().split())] for _ in range(n)]
# di = [(1,0),(-1,0),(0,1),(0,-1)]
# v = []
# shark_size, shark_exp = 2,0
# total_times = 0

# q = deque()
# for x in range(n):
#     for y in range(n):
#         if l[x][y] == 9:
#             q.append([x,y])
#             l[x][y] = 0

# def bfs(q):
#     hunt_l = []
#     time = 1
#     while not hunt_l and q:
#         next_node = deque()
#         while q:
#             x,y = q.popleft()
#             for dx,dy in di:
#                 nx,ny = x+dx,y+dy
#                 if 0 <= nx < n and 0 <= ny < n and l[nx][ny] <= shark_size:
#                     if l[nx][ny] and l[nx][ny] < shark_size:
#                         hunt_l.append([nx,ny])
#                         v[nx][ny] = time
#                     elif not hunt_l and (not l[nx][ny] or l[nx][ny] == shark_size) and not v[nx][ny]:
#                         next_node.append([nx,ny])
#                         v[nx][ny] = time
#         time += 1
#         q = next_node
#     if hunt_l:
#         hunt_l.sort()
#         return hunt_l[0], time-1
#     else: return 0,0

# while 1:
#     v = [[0]*n for _ in range(n)]
#     v[q[0][0]][q[0][1]] = 1
#     hunt, time = bfs(q)
#     if not hunt:
#         break
#     x,y = hunt
#     q = deque([[x,y]])
#     l[x][y] = 0
#     shark_exp += 1
#     total_times += time
#     if shark_exp == shark_size:
#         shark_size += 1
#         shark_exp = 0

# print(total_times)