n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((i, j, ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5))
edges.sort(key=lambda x: x[2])
res = 0
parent = [i for i in range(n)]
def find_parent(n):
    if n != parent[n]:
        parent[n] = find_parent(parent[n])
    return parent[n]
for edge in edges:
    a, b, c = edge
    if find_parent(a) != find_parent(b):
        parent[find_parent(b)] = find_parent(a)
        res += c
print(f"{res:.2f}")