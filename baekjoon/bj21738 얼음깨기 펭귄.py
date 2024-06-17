import sys
from collections import deque
input = sys.stdin.readline
n,s,p = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
def bfs(n):
    q = deque([(n,1)])
    while q:
        #print(q)
        node, depth = q.popleft()
        #print(node, path)
        for i in graph[node]:
            if i == p:
                return depth
            if not visited[i]:
                visited[i] = 1
                q.append((i,depth+1))
                
cnt = 1
for i in range(1,s+1):
    visited[i] = 1
    cnt += bfs(i)
print(n-cnt)