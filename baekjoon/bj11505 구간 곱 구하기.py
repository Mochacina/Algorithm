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
    
    def init(self,
             node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return
    
        mid = (start+end) // 2
        self.init(2*node,start,mid)
        self.init(2*node+1,mid+1,end)
        self.tree[node] = self.tree[node*2] * self.tree[node*2+1]  % 1000000007
        
    def update_value(self,
                     idx, value):
        self.data[idx] = value
        self.update(1,0,self.n-1,idx,value)
    
    def update(self,
               node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
            return self.tree[node]
        
        mid = (start+end) // 2
        if start <= idx <= mid:
            self.tree[node] = self.update(2*node,start,mid,idx,value) * self.tree[2*node+1] % 1000000007
        else:
            self.tree[node] = self.tree[2*node] * self.update(2*node+1,mid+1,end,idx,value) % 1000000007
        return self.tree[node]
    
    def query_range(self, l, r):
        return self.query(1, 0, self.n - 1, l, r)
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 1
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_query = self.query(2 * node, start, mid, l, r)
        right_query = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_query * right_query % 1000000007
    
st = SegTree(l)
res = []
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a-1: res.append(st.query_range(b-1,c-1))
    else: st.update_value(b-1,c)
sys.stdout.write('\n'.join(map(str, res)) + '\n')