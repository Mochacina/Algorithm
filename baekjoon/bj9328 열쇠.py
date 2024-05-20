from collections import deque
import copy

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(q):
    global ans
    ori_q = copy.deepcopy(q)
    next_q = deque()
    while q:
        x,y = q.popleft()
        point = building_map[x][y]
        if 65 <= ord(point) < 91 and point.lower() not in keys:
            next_q.append((x,y))
            continue
        elif point == '$': ans+=1
        elif 97 <= ord(point) < 123: keys.add(point)
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if point == '*': continue
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    
    return False if ori_q == next_q else next_q

for _ in range(int(input())):
    h,w = map(int, input().split())
    building_map = [[*input()] for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    keys = set()
    ans = 0
    
    q = deque()
    for i in range(h):
        for j in range(w):
            point = building_map[i][j]
            if (i == 0 or i == h-1) or (j == 0 or j == w-1):
                if point == '*': continue
                q.append((i,j))
                visited[i][j] = 1
    
    for i in input(): keys.add(i)
    
    while q:=bfs(q): pass
    print(ans)