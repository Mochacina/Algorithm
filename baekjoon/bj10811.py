n,m = map(int,input().split())
l = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    l[a-1:b] = reversed(l[a-1:b])
print(*l)