import sys
input = sys.stdin.readline
n,m = map(int,input().split())

class SegTree():
    def __init__(self, data) -> None:
        self.n = len(data)
        self.tree_min = [float('inf')]*(4*self.n)
        self.tree_max = [float('-inf')]*(4*self.n)
        self.data = data
        self.init(1,0,self.n-1)
    
    def init(self, node, start, end):
        if start == end:
            self.tree_min[node] = self.data[start]
            self.tree_max[node] = self.data[start]
            return
    
        mid = (start+end) // 2
        self.init(2*node,start,mid)
        self.init(2*node+1,mid+1,end)
        self.tree_min[node] = min(self.tree_min[node*2], self.tree_min[node*2+1])
        self.tree_max[node] = max(self.tree_max[node*2], self.tree_max[node*2+1])

    def query_min(self, node, start, end, left, right):
        if left > end or right < start:
            return float('inf')
        if left <= start and right >= end:
            return self.tree_min[node]
        
        mid = (start+end) // 2
        a = self.query_min(2*node,start,mid,left,right)
        b = self.query_min(2*node+1,mid+1,end,left,right)
        return min(a,b)
    
    def query_max(self, node, start, end, left, right):
        if left > end or right < start:
            return float('-inf')
        if left <= start and right >= end:
            return self.tree_max[node]
        
        mid = (start+end) // 2
        a = self.query_max(2*node,start,mid,left,right)
        b = self.query_max(2*node+1,mid+1,end,left,right)
        return max(a,b)

data = [int(input()) for _ in range(n)]
st = SegTree(data)
for _ in range(m):
    a,b = map(int,input().split())
    print(f"{st.query_min(1,0,n-1,a-1,b-1)} {st.query_max(1,0,n-1,a-1,b-1)}")