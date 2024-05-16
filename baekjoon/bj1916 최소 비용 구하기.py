import heapq

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

start, end = map(int,input().split())

distances = [float("INF")]*(n+1)
distances[start] = 0

q = [(0,start)]
while q:
    dis, node = heapq.heappop(q)
    #print(dis, node)
    
    if dis > distances[node]: continue
    for idx, dv in graph[node]:
        distance = dis + dv
        #print(f"idx: {idx}, dv: {dv}, distance: {distance}")
        if distance < distances[idx]:
            distances[idx] = distance
            #print(f"거리 갱신: {idx} / {distance}")
            heapq.heappush(q, (distance, idx))

print(distances[end])