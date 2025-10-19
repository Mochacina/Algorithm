import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c, = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])
    while q:
        now = q.popleft()
        for nxt, cost in tree[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + cost
                q.append(nxt)
    max_n = max(visited)
    return visited.index(max_n), max_n

far_node, _ = bfs(1)
_, m = bfs(far_node)
print(m)