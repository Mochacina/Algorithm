from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
times = [0]*(n+1)

for i in range(1,n+1):
    t, *l = map(int, input().split())
    times[i] = t
    for j in l[:-1]:
        graph[j].append(i)
        degree[i] += 1

q = deque()
ans = [0]*(n+1)
for i in range(1,n+1):
    if not degree[i]:
        q.append(i)
        ans[i] = times[i]

while q:
    node = q.popleft()
    for i in graph[node]:
        ans[i] = max(ans[node]+times[i], ans[i])
        degree[i] -= 1
        if not degree[i]: q.append(i)

for i in ans[1:]: print(i)