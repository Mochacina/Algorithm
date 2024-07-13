import sys
input = sys.stdin.readline

class SegTree():
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.data = data
        self.init(0, 0, self.n - 1)
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.init(2 * node + 1, start, mid) + self.init(2 * node + 2, mid + 1, end)
        return self.tree[node]

    def lazy_update(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, l, r, value):
        self._update_range(0, 0, self.n - 1, l, r, value)
    
    def _update_range(self, node, start, end, l, r, value):
        self.lazy_update(node, start, end)

        if start > r or end < l:
            return self.tree[node]
        
        if l <= start and end <= r:
            self.lazy[node] += value
            self.lazy_update(node, start, end)
            return self.tree[node]
        
        mid = (start + end) // 2
        self.tree[node] = self._update_range(node * 2 + 1, start, mid, l, r, value) + self._update_range(node * 2 + 2, mid + 1, end, l, r, value)
        return self.tree[node]
    
    def query_range(self, l, r):
        return self._query_range(0, 0, self.n - 1, l, r)
    
    def _query_range(self, node, start, end, l, r):
        self.lazy_update(node, start, end)
        
        if start > end or start > r or end < l:
            return 0
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        return self._query_range(node * 2 + 1, start, mid, l, r) + self._query_range(node * 2 + 2, mid + 1, end, l, r)

# 초기화 및 테스트
n, m, k = map(int, input().split())
st = SegTree([int(input()) for _ in range(n)])

for _ in range(m + k):
    l = [*map(int, input().split())]
    if l[0] == 1:st.update_range(l[1]-1, l[2]-1, l[3])
    else:print(st.query_range(l[1]-1, l[2]-1))