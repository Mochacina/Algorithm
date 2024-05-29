from collections import deque
n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    num, *l = map(int,input().split())
    for i in range(num-1):
        graph[l[i]].append(l[i+1])
        degree[l[i+1]] += 1

q = deque()
for i in range(1,n+1):
    if not degree[i]:
        q.append(i)

ans = []
while q:
    node = q.popleft()
    ans.append(node)
    for i in graph[node]:
        degree[i] -= 1
        if not degree[i]: q.append(i)

if len(ans) != n: print(0)
else:
    for i in ans:print(i)