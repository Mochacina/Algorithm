import sys
from collections import deque
input=sys.stdin.readline
n,m,r = map(int,input().split())
l = [[]for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    l[u].append(v)
    l[v].append(u)
l=[sorted(i,reverse=True)for i in l]
v=[0]*(n+1)
dq=deque([r])
cnt = 0
while dq:
    node = dq.popleft()
    if v[node] == 0:
        cnt += 1
        v[node] = cnt
        for nxt in l[node]:
            if not v[nxt]:dq.append(nxt)
for i in v[1:]:print(i)