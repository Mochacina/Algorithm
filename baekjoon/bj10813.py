n,m = map(int,input().split())
l = [i+1 for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    c = l[a-1]
    l[a-1] = l[b-1]
    l[b-1] = c
print(*l)