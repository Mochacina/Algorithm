# ���� �˰��� (Prim's Algorithm)
# ������ ������ �����Ͽ� ť�� �ִ´�.
# �湮�� ���� ���� ������ �� ����ġ�� �ּ��� ������ ť�� �ִ´�.
# ��� ������ ���Ե� ������ 1, 2�� �ݺ��Ѵ�.

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