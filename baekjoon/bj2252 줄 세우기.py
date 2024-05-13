from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end=' ')
    for i in graph[node]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)