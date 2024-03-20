N,M = map(int,input().split())
L = [[*map(int,input().split())] for _ in range(N)]
M = [[*map(int,input().split())] for _ in range(M)]
d = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
for i in M:
    a,b=i
    a-=1
    b-=1
    L[a][b]=1
    for j in d:
        x,y=a+j[0],b+j[1]
        if 0<=x<N and 0<=y<N and L[x][y]!=-1:L[x][y]+=1