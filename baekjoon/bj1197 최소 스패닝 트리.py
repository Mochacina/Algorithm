# v, e = map(int, input().split())
# tree = [[*map(int, input().split())] for _ in range(e)]
# tree.sort(key=lambda x: x[2])
# parent = [i for i in range(v + 1)]
# res = 0
# def find_parent(n):
#     if parent[n] != n:
#         parent[n] = find_parent(parent[n])
#     return parent[n]
# for node in tree:
#     a,b,c = node
#     if find_parent(a) != find_parent(b):
#         parent[find_parent(b)] = find_parent(a)
#         res += c
# print(res)

# import sys
# sys.setrecursionlimit(200000)  # 재귀 한도 증가
# input = sys.stdin.readline
# v, e = map(int, input().split())
# tree = [[*map(int, input().split())] for _ in range(e)]
# tree.sort(key=lambda x: x[2])  # 가중치 기준 정렬

# parent = [i for i in range(v + 1)]

# def find_parent(n):
#     if parent[n] != n:
#         parent[n] = find_parent(parent[n])  # 경로 압축
#     return parent[n]

# res = 0
# for a, b, c in tree:
#     if find_parent(a) != find_parent(b):
#         parent[find_parent(b)] = find_parent(a)
#         res += c

# print(res)

import sys
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

def union_parent(parent, rank, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    
    if root_a != root_b:
        # rank가 낮은 트리를 높은 트리 아래에 붙임
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return True
    return False

def kruskal_mst():
    v, e = map(int, input().split())
    
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    
    edges.sort()
    
    parent = [i for i in range(v + 1)]
    rank = [0] * (v + 1)
    
    mst_weight = 0
    edges_used = 0
    
    for weight, a, b in edges:
        if union_parent(parent, rank, a, b):
            mst_weight += weight
            edges_used += 1
            
            if edges_used == v - 1:
                break
    
    return mst_weight

print(kruskal_mst())