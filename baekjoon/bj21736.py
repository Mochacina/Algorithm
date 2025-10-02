from collections import deque
n,m = map(int,input().split())
l = [input() for _ in range(n)]
v = [[0]*m for _ in range(n)]
q = deque([])
pos = [(1,0),(0,1),(-1,0),(0,-1)]
for x in range(m):
    for y in range(n):
        if l[y][x] == 'I':
            q.append((x,y))
            v[y][x] = 1
cnt = 0
while q:
    x,y = q.popleft()
    if l[y][x] == 'P':
        #print("found P:",(x,y))
        cnt+=1
    for x2,y2 in pos:
        xx,yy = x+x2,y+y2
        if 0 <= xx < m and 0 <= yy < n and not v[yy][xx]:
            if l[yy][xx] != 'X':
                v[yy][xx] = 1
                q.append((xx,yy))
print(cnt if cnt > 0 else 'TT')