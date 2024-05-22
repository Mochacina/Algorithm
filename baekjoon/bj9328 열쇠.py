from collections import deque

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(q):
    global ans
    next_q = deque()
    while q:
        x,y = q.popleft()
        p = bMap[x][y]
        if 'A' <= p <= 'Z' and p.lower() not in keys:
            next_q.append((x,y))
            continue
        elif p == '$': ans+=1
        elif 'a' <= p <= 'z':
            keys.add(p)
            q.extend(next_q)
            next_q.clear()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if p == '*': continue
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    
    return next_q

for _ in range(int(input())):
    h,w = map(int, input().split())
    bMap = [[*input()] for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    keys = set()
    ans = 0
    
    q = deque()
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == h-1) or (j == 0 or j == w-1):
                if bMap[i][j] == '*': continue
                q.append((i,j))
                visited[i][j] = 1
    
    for i in input(): keys.add(i)
    
    while bfs(q): pass
    print(ans)