import sys
from collections import deque
i=sys.stdin.readline
n,s,p=map(int,i().split())
v=[0]*(n+1)
v[p]=1
l=[[]for _ in range(n+1)]
for _ in range(n-1):
 A,B=map(int,i().split())
 l[A].append(B)
 l[B].append(A)
q=deque([(p,0)])
a=[]
while q:
 j,c = q.popleft()
 for k in l[j]:
  if not v[k] and len(a)<2:
   if k <= s:a.append(c+1)
   else:v[k]+=1;q.append((k,c+1))
print(n-sum(a,1))