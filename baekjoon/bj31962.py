n,x=map(int,input().split())
d=-1
for _ in range(n):
    s,t=map(int,input().split())
    if s+t <= x: d=max(d,s)
print(d)