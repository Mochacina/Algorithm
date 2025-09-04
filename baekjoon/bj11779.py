import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, end, n, graph):
    INF = float('inf')
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for next_city, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < dist[next_city]:
                dist[next_city] = new_cost
                parent[next_city] = now
                heapq.heappush(heap, (new_cost, next_city))

    return dist, parent

def get_path(parent, start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

n = int(input().strip())        # 도시 개수
m = int(input().strip())        # 버스 개수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dist, parent = dijkstra(start, end, n, graph)
path = get_path(parent, start, end)

print(dist[end])       # 최소 비용
print(len(path))       # 경로에 포함된 도시 개수
print(*path)           # 실제 경로 출력

