n,m = map(int,input().split())
l = [0]*n
for i in range(m):
    a,b,c = map(int,input().split())
    for i in range(a-1,b): l[i] = c
print(*l)