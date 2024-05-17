n,m = map(int,input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    cities[a].append([b,c])

distances = [float("INF")]*(n+1)
distances[1] = 0

