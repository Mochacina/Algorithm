import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())

inf = float("inf")

l = [[inf]*(n)for _ in range(n)]
for i in range(n): l[i][i] = 0
items = list(map(int, input().split()))

for _ in range(r):
    a,b,c = map(int,input().split())
    a,b=a-1,b-1
    l[a][b] = min(l[a][b], c)
    l[b][a] = min(l[b][a], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            l[j][k] = min(l[j][k], l[i][k]+l[j][i])
    
distances = [[j if j!=inf else inf for j in dis]for dis in l]
print(max([sum([items[num] if dis <= m else 0 for num, dis in enumerate(di)]) for di in distances]))
