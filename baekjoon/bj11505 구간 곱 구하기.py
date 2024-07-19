import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
l = [int(input())for _ in range(n)]

class SegTree():
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0]*(4*n)
        self.data = data
        self.init(1,0,self.n-1)
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return
    
        mid = (start+end) // 2
        self.init(2*node,start,mid)
        self.init(2*node+1,mid+1,end)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
        
    def update_value(self, idx, value):
        diff = value - self.data[idx]
        self.data[idx] = value
        self.update(1,0,self.n-1,idx,diff)
    
    def update(self, node, start, end, idx, diff):
        if idx < start or end < idx: return
        self.tree[node] += diff
        if start != end:
            mid = (start+end) // 2
            self.update(2*node,start,mid,idx,diff)
            self.update(2*node+1,mid+1,end,idx,diff)