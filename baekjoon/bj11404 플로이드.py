n = int(input())
m = int(input())

inf = float("inf")
l = [[inf]*(n)for _ in range(n)]
for i in range(n): l[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    a,b=a-1,b-1
    l[a][b] = min(l[a][b], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            l[j][k] = min(l[j][k], l[i][k]+l[j][i])

for i in l: print(*[j if j!=inf else 0 for j in i])