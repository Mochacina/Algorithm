# from collections import deque

# n,m = map(int, input().split())
# l = [[*map(int, input().split())]for _ in range(n)]
# v = [[0]*m for _ in range(n)]
# di = [(0,1),(1,0),(-1,0),(0,-1)]
# air_q = deque([(0,0)])
# cheese_q = deque()
# times = 0

# def find_cheese(q):
#     cheeses = deque()
#     while q:
#         x,y = q.popleft()
#         for dx,dy in di:
#             nx,ny = x+dx,y+dy
#             if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
#                 if l[nx][ny]:
#                     cheeses.append((nx,ny))
#                 else:
#                     l[nx][ny] = -1
#                     q.append((nx,ny))
#                 v[nx][ny] = 1
#     return cheeses

# def melt_cheese(q):
#     air = deque()
#     while q:
#         x,y = q.popleft()
#         cnt=0
#         for dx,dy in di:
#             nx,ny = x+dx,y+dy
#             if 0 <= nx < n and 0 <= ny < m and l[nx][ny]==-1:
#                 cnt += 1
#         if cnt >= 2:air.append((x,y))
#         else: v[x][y] = 0
#     for x,y in air: l[x][y] = -1
#     return air

# while cheese_q:=find_cheese(air_q):
#     air_q=melt_cheese(cheese_q)
#     times += 1
# print(times)

n,m = map(int, input().split())
l = [[*map(int, input().split())]for _ in range(n)]
di = [(0,1),(1,0),(-1,0),(0,-1)]
air_q = [(0,0)]
cheese_q = []
times = 0

def find_cheese(q):
    cheeses = []
    while q:
        x,y = q.pop()
        for dx,dy in di:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if l[nx][ny]==1:
                    l[nx][ny]=2
                    cheeses.append((nx,ny))
                elif l[nx][ny]==0:
                    l[nx][ny]=-1
                    q.append((nx,ny))
    return cheeses

def melt_cheese(q):
    air = []
    while q:
        x,y = q.pop()
        cnt=0
        for dx,dy in di:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and l[nx][ny]==-1: cnt += 1
        if cnt >= 2:air.append((x,y))
        else: l[x][y]=1
    for x,y in air: l[x][y] = -1
    return air

while cheese_q:=find_cheese(air_q):
    air_q=melt_cheese(cheese_q)
    times += 1
print(times)