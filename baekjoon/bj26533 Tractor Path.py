n = int(input())
l = [[*input()]for _ in range(n)]
v = [[0]*n for _ in range(n)]
di = [(0,1),(1,0)]
q = [(0,0)]
while q:
    x,y = q.pop()
    if x+y==n*2-2: exit(print('Yes'))
    for dx,dy in di:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and l[nx][ny]=='.':
            l[nx][ny] = 'x'
            q.append((nx,ny))
print('No')