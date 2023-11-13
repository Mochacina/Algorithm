import sys
from collections import deque

m,n,h = map(int,input().split())
di = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
dq = deque([])

l = []

for i in range(h):
    l2 = []
    for j in range(n):
        l2.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if l2[j][k]==1:dq.append([i,j,k])
    l.append(l2)
    
while dq:
    a,b,c = dq.popleft()
    
    for i in di:
        x = a+i[0]
        y = b+i[1]
        z = c+i[2]
        
        if 0<=x<h and 0<=y<n and 0<=z<m and l[x][y][z] == 0:
            dq.append([x,y,z])
            l[x][y][z] = l[a][b][c]+1
          
maxN = 0  
for i in l:
    for j in i:
        if 0 in j:print(-1);exit()
        maxN = max(maxN,max(j))
        
print(maxN-1 if (maxN > 1) else 0)