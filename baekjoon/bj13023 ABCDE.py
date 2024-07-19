import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, cnt, visited):
    if cnt >= 5: exit(print(1))
    visited[node] = 1
    for nghb in graph[node]:
        if not visited[nghb]:
            if dfs(nghb, cnt+1, visited): return 1
    visited[node] = 0
    return 0    

for i in range(n):
    visited = [0]*n
    visited[i] = 1
    dfs(i, 1, visited)
print(0)