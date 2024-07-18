import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    nodes = [(node,1)]
    while nodes:
        nd, cnt = nodes.pop()
        if cnt >= 5: exit(print(1))
        for i in graph[nd]:
            if not visited[i]:
                nodes.append((i,cnt+1))

for i in range(n):
    visited = [0]*n
    visited[i] = 1
    dfs(i)
print(0)