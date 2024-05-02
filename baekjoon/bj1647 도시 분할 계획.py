n,m = map(int, input().split())
l = [[*map(int, input().split())] for _ in range(m)]
l.sort(key=lambda x:x[2])
s, nl = 0, 0
parent = [i for i in range(n+1)]
def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]
for n in l:
    a,b,c = n
    if find(a) != find(b):
        parent[find(b)] = find(a)
        s += c
        nl = c
print(s-nl)

# v, e = map(int, input().split())
# tree = [[*map(int, input().split())] for _ in range(e)]
# tree.sort(key=lambda x: x[2])
# parent = [i for i in range(v + 1)]
# res, l = 0, 0
# def find_parent(n):
#     if parent[n] != n:
#         parent[n] = find_parent(parent[n])
#     return parent[n]
# for node in tree:
#     a,b,c = node
#     if find_parent(a) != find_parent(b):
#         parent[find_parent(b)] = find_parent(a)
#         res += c
#         l = c
# print(res-l)

# import sys
# n, m = map(int, input().split())
# tree = [[*map(int, sys.stdin.readline().split())] for _ in range(m)]
# tree.sort(key=lambda x: x[2])
# parent = [i for i in range(n + 1)]
# res, l = 0, 0
# def find_parent(n):
#     if parent[n] != n:
#         parent[n] = find_parent(parent[n])
#     return parent[n]
# for node in tree:
#     a,b,c = node
#     if find_parent(a) != find_parent(b):
#         parent[find_parent(b)] = find_parent(a)
#         res += c
#         l = c
# print(res-l)