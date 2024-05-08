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
    for i in range(6):
        f = node+i+1
        if f > 99: exit(print(cnt+1))
        if l[f]: f = l[f]
        if not v[f]:
            v[f] = cnt+1
            q.append((f, cnt+1))