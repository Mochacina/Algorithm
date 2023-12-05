# for _ in range(int(input())):
#     m,n,k = map(int,input().split())
#     l = [[0]*m for _ in range(n)]
#     baechu = [list(map(int,input().split()))for _ in range(k)]
#     for b in baechu:
#         x,y = b
#         l[y][x] = 1
#     level = 0
#     for i in l:print(i)
#     while sum([sum(i)for i in l])<m*n:
#         level += 1
#         v = [[0]*m for _ in range(n)]
#         for y in range(n):
#             for x in range(m):
#                 if l[y][x] == 1 and not v[y][x]:
#                     v[y][x] = 1
#                     stack = [[x,y]]
#                     while stack:
#                         node = stack.pop()
#                         xx, yy = node
#                         for di in [(1,0),(-1,0),(0,1),(0,-1)]:
#                             dx, dy = di
#                             x2,y2 = dx+xx,dy+yy
#                             if 0 <= x2 < m and 0 <= y2 < n and not v[y2][x2]:
#                                 l[y2][x2]=1
#                                 v[y2][x2]=1
#                                 stack.append([x2,y2])
#     print(level)

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    l = [[0]*m for _ in range(n)]
    for b in range(k):
        x,y = map(int,input().split())
        l[y][x] = 1
    v = [[0]*m for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(m):
            if l[y][x] and not v[y][x]:
                cnt += 1
                v[y][x] = 1
                stack = [[x,y]]
                while stack:
                    xx,yy = stack.pop()
                    for di in [(1,0),(-1,0),(0,1),(0,-1)]:
                        dx, dy = di
                        x2,y2 = dx+xx,dy+yy
                        if 0 <= x2 < m and 0 <= y2 < n and l[y2][x2] and not v[y2][x2]:
                            v[y2][x2]=1
                            stack.append([x2,y2])
    print(cnt)