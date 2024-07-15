# import sys
# input = sys.stdin.readline
# n,m,k = map(int,input().split())

# class SegTree():
#     def __init__(self, data) -> None:
#         self.n = len(data)
#         self.tree = [0]*(4*n)
#         self.data = data
#         self.init(0,0,self.n-1)
    
#     def init(self, node, start, end):
#         if start == end:
#             self.tree[node] = self.data[start]
#             return
    
#         mid = (start+end) // 2
#         self.init(2*node+1,start,mid)
#         self.init(2*node+2,mid+1,end)
#         self.tree[node] = self.tree[node*2+1] + self.tree[node*2+2]
    
#     def update_value(self, idx, value):
#         diff = value - self.data[idx]
#         self.data[idx] = value
#         self.update(0,0,self.n-1,idx,diff)
    
#     def update(self, node, start, end, idx, diff):
#         if idx < start or end < idx: return
#         self.tree[node] += diff
#         if start != end:
#             mid = (start+end) // 2
#             self.update(2*node+1,start,mid,idx,diff)
#             self.update(2*node+2,mid+1,end,idx,diff)
    
#     def query(self, node, start, end, left, right):
#         if left > end or right < start:
#             return 0
#         if left <= start and right >= end:
#             return self.tree[node]
        
#         mid = (start+end) // 2
#         a = self.query(2*node+1,start,mid,left,right)
#         b = self.query(2*node+2,mid+1,end,left,right)
#         return a+b

# st = SegTree([int(input()) for _ in range(n)])

# for _ in range(m+k):
#     a,b,c = map(int,input().split())
#     if a-1: print(st.query(0,0,n-1,b-1,c-1))
#     else: st.update_value(b-1,c)

import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())

class SegTree():
    def __init__(self, data) -> None:
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
    
    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        
        mid = (start+end) // 2
        a = self.query(2*node,start,mid,left,right)
        b = self.query(2*node+1,mid+1,end,left,right)
        return a+b

st = SegTree([int(input()) for _ in range(n)])

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a-1: print(st.query(1,0,n-1,b-1,c-1))
    else: st.update_value(b-1,c)