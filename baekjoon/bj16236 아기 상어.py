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
    # ��Ƹ��� ����� ���� ���� �湮�� ������ ������ ��� ���ư�
    while not hunt_l and q:
        next_node = deque()
        while q:
            x,y = q.popleft()
            for dx,dy in di:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n and l[nx][ny] <= shark_size:
                    # ��Ƹ��� �� �ִ� ����� �ִ� ��� ������ ���� ��Ƹ���
                    if l[nx][ny] and l[nx][ny] < shark_size:
                        hunt_l.append([nx,ny])
                        v[nx][ny] = time
                    # ��Ƹ��� �� �ִ� ����� ���� ���, �湮���� ���� �� ���� �̵�
                    elif not hunt_l and (not l[nx][ny] or l[nx][ny] == shark_size) and not v[nx][ny]:
                        next_node.append([nx,ny])
                        v[nx][ny] = time
        time += 1
        q = next_node
    if hunt_l:
        # ���� �ִ³� ���ʿ� �ִ³� �켱 ��Ƹ���
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

from collections import deque
n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
di = [(1,0),(-1,0),(0,1),(0,-1)]
shark_size, shark_exp = 2, 0
total_times = 0

q = deque()
for x in range(n):
    for y in range(n):
        if l[x][y] == 9:
            q.append([x,y]);l[x][y] = 0

def bfs(q):
    hunt_l = []
    time = 0
    v = [[0]*n for _ in range(n)]  # BFS�� ������ ���� �ʱ�ȭ
    while not hunt_l and q:
        next_node = deque()
        while q:
            x, y = q.popleft()
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and l[nx][ny] <= shark_size:
                    v[nx][ny] = time
                    if 0 < l[nx][ny] < shark_size:hunt_l.append([nx, ny])
                    elif not hunt_l:next_node.append([nx, ny])
        q = next_node
        time += 1
    if hunt_l:
        hunt_l.sort()
        return hunt_l[0], time
    else:return [], 0

while q:
    hunt, time = bfs(q)
    if not hunt:break
    x, y = hunt
    q = deque([[x, y]])
    l[x][y] = 0
    shark_exp += 1
    total_times += time
    if shark_exp == shark_size:
        shark_size += 1;shark_exp = 0

print(total_times)