import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int,input().split())
l = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    l[u].append(v)
    l[v].append(u)
l = [sorted(row) for row in l]
dq,k = deque([r]),1
while dq:
    d = dq.pop()
    if visited[d] == 0:
        visited[d] = k
        k += 1
        for i in l[d]:
            if visited[i] == 0:dq.append(i)
for i in visited[1:]:print(i)