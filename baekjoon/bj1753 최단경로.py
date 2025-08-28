import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, V):
    distance = [INF] * (V + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 노드)

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:  # 이미 처리된 경우 무시
            continue
        for nxt, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[nxt]:
                distance[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

    return distance

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = dijkstra(K, graph, V)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])