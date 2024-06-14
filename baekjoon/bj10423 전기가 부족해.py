import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
power = [*map(int,input().split())]
tree = [[*map(int, input().split())] for _ in range(m)]
tree.sort(key=lambda x: x[2])
parent = [i for i in range(n+1)]
for i in power: parent[i] = power[0]
ans = 0
def f(i):
    if i != parent[i]:
        parent[i] = f(parent[i])
    return parent[i]
for a,b,c in tree:
    if f(a) != f(b):
        parent[f(b)] = parent[a]
        ans += c
print(ans)