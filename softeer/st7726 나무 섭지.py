from collections import deque

dir = [(0,1),(1,0),(-1,0),(0,-1)]
n, m = map(int, input().split())
l = [[*input()] for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q_n,q_d = deque(),deque()

for i in range(n):
    for j in range(m):
        if l[i][j] == 'D': q_d.append((i,j,0))
        elif l[i][j] == 'N': q_n.append((i,j,0))

def bfs(q, isMan):
    while q:
        x,y,cnt = q.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] < isMan:
                if isMan == 1:
                    if l[nx][ny]=='#':continue
                    elif l[nx][ny]=='D':return cnt+1
                if isMan == 2 and l[nx][ny]=='G':return cnt+1
                visited[nx][ny] = isMan
                q.append((nx,ny,cnt+1))
    return 9e9

print(["No","Yes"][bfs(q_n, 1) < bfs(q_d,2)])