import heapq

def dkstr(grph, start):
    distances = [float("INF")]*(n+1)
    distances[start] = 0

    q = [(0,start)]
    while q:
        dis, node = heapq.heappop(q)
        
        if dis > distances[node]: continue
        for neib, neib_dis in grph[node]:
            total_dis = dis + neib_dis
            if total_dis < distances[neib]:
                distances[neib] = total_dis
                heapq.heappush(q, (total_dis, neib))
                
    return distances

n,m,x = map(int,input().split())
graph, r_graph = [[] for _ in range(n+1)],[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    r_graph[b].append((a,c))

#print(dkstr(graph, x))
#print(dkstr(r_graph, x))
dis1 = dkstr(graph, x)
dis2 = dkstr(r_graph, x)

print(max([dis1[i]+dis2[i] for i in range(1,n+1)]))