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
        self.tree[node] = self.tree[node*2] * self.tree[node*2+1]
        
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
            self.tree[node] = self.update(2*node,start,mid,idx,value) * self.tree[2*node+1]
        else:
            self.tree[node] = self.tree[2*node] * self.update(2*node+1,mid+1,end,idx,value)
        return self.tree[node]
    
st = SegTree(l)
print(st.tree)
st.update_value(3, 6)
print(st.tree)