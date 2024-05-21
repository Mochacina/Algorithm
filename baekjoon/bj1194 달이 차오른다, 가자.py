from collections import deque
dir = [(0,1),(1,0),(0,-1),(-1,0)]

n,m = map(int,input().split())
li = [[*input()] for _ in range(n)]
d_key = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}
visited = [[[0]*(1<<6) for _ in range(m)] for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if li[i][j] == '0':
            q.append((0,0,i,j))
            visited[i][j][0] = 1

while q:
    keys, cnt, x, y = q.popleft()
    
    for dx,dy in dir:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny][keys] and li[nx][ny] != '#':
            if 'A' <= li[nx][ny] <= 'F' and not (keys & d_key[li[nx][ny].lower()]):
                continue
            if li[nx][ny] == '1':
                exit(print(cnt+1))
            if li[nx][ny] in d_key:
                n_keys = keys | d_key[li[nx][ny]]
                visited[nx][ny][n_keys] = 1
                q.append((n_keys,cnt+1,nx,ny))
            else:
                visited[nx][ny][keys] = 1
                q.append((keys,cnt+1,nx,ny))

print(-1)