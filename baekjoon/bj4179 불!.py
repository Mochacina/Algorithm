from collections import deque
dir = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(q):
    while q:
        type, x, y, cnt = q.popleft()
        if type == 'J':
            cnt+=1
            if x in [0,r-1] or y in [0,c-1]:
                return cnt
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0 <= nx < r and 0 <= ny < c and l[nx][ny] not in ['#','F',type]:
                l[nx][ny] = type
                q.append((type,nx,ny,cnt))
    return "IMPOSSIBLE"

r,c = map(int,input().split())
l = [[*input()]for _ in range(r)]
q = deque()
for i in range(r):
    for j in range(c):
        if l[i][j] == 'F': q.appendleft(('F',i,j,0))
        elif l[i][j] == 'J': q.append(('J',i,j,0))
print(bfs(q))