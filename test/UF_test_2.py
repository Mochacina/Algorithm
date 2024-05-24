import time
import random

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return False
        else:
            return True

class UnionFindNoRank:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.parent[rootY] = rootX
            return False
        else:
            return True

def simulate_worst_case_union_find(n, use_rank=True):
    if use_rank:
        uf = UnionFind(n)
    else:
        uf = UnionFindNoRank(n)

    # Worst case: union in a linear chain manner
    start_time = time.time()
    for i in range(1, n):
        uf.union(i - 1, i)
    end_time = time.time()

    return end_time - start_time

n = 50000

time_with_rank = simulate_worst_case_union_find(n, use_rank=True)
time_without_rank = simulate_worst_case_union_find(n, use_rank=False)

print(f"Time with rank (worst case): {time_with_rank:.6f} seconds")
print(f"Time without rank (worst case): {time_without_rank:.6f} seconds")
