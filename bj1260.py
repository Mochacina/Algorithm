#from collections import defaultdict


# DFS 함수
def dfs(graph, start):
    visited = []  # 방문한 노드를 저장할 리스트
    stack = [start]  # 스택에 시작 노드를 넣어줍니다.

    while stack:
        node = stack.pop()  # 스택에서 노드를 하나씩 꺼냅니다.
        if node not in visited:  # 방문하지 않은 경우에만 처리합니다.
            visited.append(node)  # 방문한 노드를 추가합니다.
            stack.extend(sorted(graph[node], reverse=True))  # 해당 노드와 연결된 노드들을 스택에 추가합니다.

    return visited


# BFS 함수
def bfs(graph, start):
    visited = []  # 방문한 노드를 저장할 리스트
    queue = [start]  # 큐에 시작 노드를 넣어줍니다.

    while queue:
        node = queue.pop(0)  # 큐에서 노드를 하나씩 꺼냅니다.
        if node not in visited:  # 방문하지 않은 경우에만 처리합니다.
            visited.append(node)  # 방문한 노드를 추가합니다.
            queue.extend(sorted(graph[node]))  # 해당 노드와 연결된 노드들을 큐에 추가합니다.

    return visited


# 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 순서로 연결된 간선 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 수행 결과 출력
dfs_result = dfs(graph, V)
print(' '.join(map(str, dfs_result)))

# BFS 수행 결과 출력
bfs_result = bfs(graph, V)
print(' '.join(map(str, bfs_result)))