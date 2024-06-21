n,m,k = map(int,input().split())
l = [int(input()) for _ in range(n)]

class SegTree():
    def __init__(self, data) -> None:
        self.n = len(data)
        self.tree = [0]*(4*n)
        self.data = data
        self.init(0,0,n-1)
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return
    
        mid = (start+end) // 2
        self.init(2*node+1,start,mid)
        self.init(2*node+2,mid+1,end)
        self.tree[node] = self.tree[node*2+1] + self.tree[node*2+2]

st = SegTree(l)
print(st.tree)