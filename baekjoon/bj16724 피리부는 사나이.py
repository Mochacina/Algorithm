di = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
n,m = map(int,input().split())
l = [[*input()]for _ in ' '*n]
v = [[-1]*m for _ in ' '*n]
cnt = 0

def dfs(x,y,idx):
    global cnt
    if v[x][y] != -1:
        if v[x][y] == idx: cnt += 1
        return
    v[x][y] = idx
    dx,dy = di[l[x][y]]
    nx,ny = x+dx,y+dy
    dfs(nx,ny,idx)

for i in range(n):
    for j in range(m):
        if v[i][j] == -1: dfs(i,j,i*m+j)
print(cnt)

# di = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
# n,m = map(int,input().split())
# l = [[*input()]for _ in ' '*n]
# v = [[-1]*m for _ in ' '*n]
# cnt = 0

# def dfs(x,y,idx):
#     global cnt
#     dx,dy = di[l[x][y]]
#     nx,ny = x+dx,y+dy
#     if v[nx][ny] != -1:
#         if v[nx][ny] == idx: cnt += 1
#     else:
#         v[nx][ny] = idx
#         dfs(nx,ny,idx)

# for i in range(n):
#     for j in range(m):
#         if v[i][j] == -1:
#             v[i][j] = i*m+j
#             dfs(i,j,i*m+j)

# print(cnt)