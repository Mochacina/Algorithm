R=range
n,m=map(int,input().split())
l=[list(map(int,input().split()))for _ in R(n)]
di=[(-1,0),(1,0),(0,-1),(0,1)]
y=0
def bfs(a,b):
 s=[(a,b)];v[b][a]=1
 while s:
  c=0;x,y=s.pop()
  for d in di:
   x2=x+d[0];y2=y+d[1]
   if 0<=x2<m and 0<=y2<n:
    if l[y2][x2]==0:c+=1
    elif not v[y2][x2]:v[y2][x2]=1,s.append((x2,y2))
  l_cp[y][x]=0 if l[y][x]-c<=0 else l[y][x]-c
 return 1
while sum([sum(l2)for l2 in l]):
 v=[[0]*m for _ in R(n)]
 l_cp=[[0]*m for _ in R(n)]
 op=[bfs(j,i)for j in R(m)for i in R(n)if l[i][j]!=0 and v[i][j]==0]
 if(len(op)>=2):print(y);exit()
 y+=1;l=l_cp
print(0)