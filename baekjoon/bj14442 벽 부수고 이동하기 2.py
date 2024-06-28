from collections import deque
n,m,k = map(int,input().split())
l = [[*input()] for _ in range(n)]
q = deque([(0,0,0,1)])
visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = 1

while q:
    cnt,x,y,turn = q.popleft()
    if x==n-1 and y==m-1: exit(print(turn))
    
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if l[nx][ny] == '0' and not visited[cnt][nx][ny]:
                q.append((cnt,nx,ny,turn+1))
                visited[cnt][nx][ny] = 1
            elif cnt < k and l[nx][ny] == '1' and not visited[cnt+1][nx][ny]:
                q.append((cnt+1,nx,ny,turn+1))
                visited[cnt+1][nx][ny] = 1
print(-1)