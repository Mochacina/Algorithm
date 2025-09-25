import sys
from collections import deque

input = sys.stdin.readline

N, R, Q = map(int, input().split())

# 1. 인접 리스트 생성 (양방향)
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 2. BFS로 트리 구조 만들기
tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
order = []  # BFS 순서 저장

q = deque([R])
visited[R] = True

while q:
    cur = q.popleft()
    order.append(cur)
    for nxt in adj[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            tree[cur].append(nxt)
            q.append(nxt)

# 3. 서브트리 크기 계산 (Bottom-up)
subtree_size = [0] * (N + 1)

for u in reversed(order):  # 리프부터 처리
    size = 1  # 자기 자신 포함
    for v in tree[u]:
        size += subtree_size[v]
    subtree_size[u] = size

# 4. 쿼리 처리
for _ in range(Q):
    u = int(input())
    print(subtree_size[u])
