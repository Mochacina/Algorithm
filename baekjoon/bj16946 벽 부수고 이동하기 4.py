# n, m = map(int, input().split())
# l = [[int(i) for i in input()] for _ in range(n)]
# v = [[0]*m for _ in range(n)]
# c = [[0]*m for _ in range(n)]
# di = [(0,1),(0,-1),(1,0),(-1,0)]

# def dfs(x, y):
#     q, cnt_q = [(x,y)], [(x,y)]
#     cnt = 1
#     v[x][y] = (x,y)
#     while q:
#         x,y = q.pop()
#         for dx,dy in di:
#             nx,ny = x+dx,y+dy
#             if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 0 and v[nx][ny] == 0:
#                 q.append((nx,ny))
#                 cnt_q.append((nx,ny))
#                 v[nx][ny] = (x,y)
#                 cnt += 1
#     for x,y in cnt_q: c[x][y] = cnt
        
# for i in range(n):
#     for j in range(m):
#         if l[i][j] == 0 and v[i][j] == 0:
#             dfs(i, j)

# for i in range(n):
#     for j in range(m):
#         if l[i][j] == 1:
#             s = set()
#             for dx,dy in di:
#                 nx,ny = i+dx,j+dy
#                 if 0 <= nx < n and 0 <= ny < m and c[nx][ny] >= 1 and v[nx][ny] not in s:
#                     s.add(v[nx][ny])
#                     l[i][j] += c[nx][ny]
#             l[i][j] %= 10
            
# for i in l:
#     print(*i, sep='')

n, m = map(int, input().split())
l = [[int(i) for i in input()] for _ in range(n)]
v = [[0]*m for _ in range(n)]
c = [[0]*m for _ in range(n)]
di = [(0,1),(0,-1),(1,0),(-1,0)]
region_id = 1

def dfs(x, y):
    q, cnt_q = [(x,y)], [(x,y)]
    cnt = 1
    v[x][y] = region_id
    while q:
        x,y = q.pop()
        for dx,dy in di:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 0 and v[nx][ny] == 0:
                q.append((nx,ny))
                cnt_q.append((nx,ny))
                v[nx][ny] = region_id
                cnt += 1
    for x,y in cnt_q: c[x][y] = cnt

for i in range(n):
    for j in range(m):
        if l[i][j] == 0 and v[i][j] == 0:
            dfs(i, j)
            region_id += 1

for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            s = set()
            for dx,dy in di:
                nx,ny = i+dx,j+dy
                if 0 <= nx < n and 0 <= ny < m and c[nx][ny] >= 1:
                    r_id = v[nx][ny]
                    if r_id not in s:
                        s.add(r_id)
                        l[i][j] += c[nx][ny]
            l[i][j] %= 10

for i in l: print(*i, sep='')