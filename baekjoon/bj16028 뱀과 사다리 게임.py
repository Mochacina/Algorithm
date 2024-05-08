from collections import deque

n,m = map(int, input().split())
l = [0]*101
v = [0]*101
for _ in range(n+m):
    x,y = map(int, input().split())
    l[x] = y

q = deque([(1,0)])
while q:
    node, cnt = q.popleft()
    if node == 100: break
    for i in [1,2,3,4,5,6]:
        fwd = node+i
        if fwd > 100: break
        if l[fwd]: fwd = l[fwd]
        if not v[fwd]:
            v[fwd] = cnt+1
            q.append((fwd, cnt+1))
            
print(v[100])
