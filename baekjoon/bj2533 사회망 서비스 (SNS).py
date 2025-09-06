import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 양방향 그래프로 우선 친구 관계를 저장
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# dp[i][0]: i번 노드가 얼리 아답터가 아닐 때
# dp[i][1]: i번 노드가 얼리 아답터일 때
dp = [[0, 0] for _ in range(N + 1)]

# BFS를 위한 방문 기록
visited = [False] * (N + 1)

# BFS 순서를 저장할 리스트
order = []

# 부모-자식 관계를 저장할 트리
tree = [[] for _ in range(N + 1)]

# 1. BFS를 통해 트리 구조를 만들고, 탐색 순서를 저장한다.
q = deque([1])
visited[1] = True

while q:
    current_node = q.popleft()
    order.append(current_node)
    
    for neighbor in adj[current_node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            # current_node를 부모로, neighbor를 자식으로 설정
            tree[current_node].append(neighbor)
            q.append(neighbor)

print("tree:", tree)
print("order", q)

# 2. BFS 탐색 순서를 거꾸로 돌면서 DP 값을 계산한다. (Bottom-up 방식)
# 이렇게 하면 항상 자식 노드가 부모보다 먼저 계산된다!
for u in reversed(order):
    # 디버그 로그: 어떤 순서로 계산하는지 똑똑히 보라구!
    # print(f"DEBUG: Calculating DP for node {u}")
    
    dp[u][1] = 1  # u가 얼리 아답터인 경우, 기본 비용 1
    dp[u][0] = 0  # u가 얼리 아답터가 아닌 경우, 기본 비용 0

    for v in tree[u]: # u의 모든 자식 v에 대하여
        # 점화식은 그대로!
        # u가 얼리 아답터가 아니면 -> 자식 v는 무조건 얼리 아답터여야 함
        dp[u][0] += dp[v][1]
        # u가 얼리 아답터이면 -> 자식 v는 얼리 아답터이거나 아니거나, 더 싼 쪽으로!
        dp[u][1] += min(dp[v][0], dp[v][1])

# 루트 노드(1번)의 두 경우 중 최소값을 출력
print(min(dp[1][0], dp[1][1]))