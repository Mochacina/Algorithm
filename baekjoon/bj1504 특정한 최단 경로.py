import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for nxt, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[nxt]:
                distance[nxt] = new_dist
                heapq.heappush(heap, (new_dist, nxt))
    return distance

# 입력
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 다익스트라 실행
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로 1: 1 → v1 → v2 → N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

# 경로 2: 1 → v2 → v1 → N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)

# 도달 불가 시 -1 출력
print(result if result < INF else -1)