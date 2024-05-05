v, e = map(int, input().split())
tree = [[*map(int, input().split())] for _ in range(e)]
tree.sort(key=lambda x: x[2])
parent = [i for i in range(v + 1)]
res = 0
def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]
for node in tree:
    a,b,c = node
    if find_parent(a) != find_parent(b):
        parent[find_parent(b)] = find_parent(a)
        res += c
print(res)