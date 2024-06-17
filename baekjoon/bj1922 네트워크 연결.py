# 프림 알고리즘 (Prim's Algorithm)
# 임의의 정점을 선택하여 큐에 넣는다.
# 방문한 적이 없는 정점들 중 가중치가 최소인 정점을 큐에 넣는다.
# 모든 정점이 포함될 때까지 1, 2를 반복한다.

import heapq

n = int(input())
m = int(input())

l = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    l[a].append((c, b))
    l[b].append((c, a))

v = [0]*(n+1)
q = [(0,1)]
ans = 0

while q:
    w, node = heapq.heappop(q)
    
    if v[node]: continue
    v[node] = 1
    
    ans += w
    for n_w, n_node in l[node]:
        if not v[n_node]: heapq.heappush(q, (n_w, n_node))

print(ans)