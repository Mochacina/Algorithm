import sys
from collections import deque

input = sys.stdin.readline

n,r,Q = map(int,input().split())

adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

#print("adj:", adj)

tree = [[] for _ in range(n+1)]
visited = [0]*(n+1)
order = []

q = deque([r])
visited[r] = 1

while q:
    node = q.popleft()
    order.append(node)
    for nxt in adj[node]:
        if not visited[nxt]:
            visited[nxt] = 1
            tree[node].append(nxt)
            q.append(nxt)

#print("tree:", tree)

subtree = [0]*(n+1)

for u in reversed(order):
    size = 1
    for v in tree[u]:
        size += subtree[v]
    subtree[u] = size

for _ in range(Q):
    u = int(input())
    print(subtree[u])