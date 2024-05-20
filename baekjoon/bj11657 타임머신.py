# n,m = map(int,input().split())
# cities = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     cities[a].append([b,c])

# distances = [float("INF")]*(n+1)
# distances[1] = 0

# for t in range(n):
#     for i in range(1,n+1):
#         for city, w in cities[i]:
#             if distances[i] == float("INF"): continue
#             if distances[i]+w < distances[city]:
#                 distances[city] = distances[i]+w

# for i in range(1,n+1):
#     for city, w in cities[i]:
#         if distances[i] == float("INF"): continue
#         if distances[i]+w < distances[city]:
#             exit(print(-1))

# for i in distances[2:]:
#     print(i if i!=float("INF") else -1)
    
n,m = map(int,input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    cities[a].append([b,c])

distances = [float("INF")]*(n+1)
distances[1] = 0

for t in range(n):
    for i in range(1,n+1):
        for city, w in cities[i]:
            if distances[i] == float("INF"): continue
            if distances[i]+w < distances[city]:
                if t==n-1:exit(print(-1))
                distances[city] = distances[i]+w

for i in distances[2:]:
    print(i if i!=float("INF") else -1)