from collections import deque

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(q):
    global ans
    next_q = deque()
    while q:
        x,y = q.popleft()
        pt = bMap[x][y]
        if 65 <= ord(pt) < 91 and pt.lower() not in keys:
            next_q.append((x,y))
            continue
        elif pt == '$': ans+=1
        elif 97 <= ord(pt) < 123:
            keys.add(pt)
            q.extend(next_q)
            next_q.clear()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if pt == '*': continue
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    
    return len(next_q)

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