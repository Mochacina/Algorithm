import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
rank = [0]*n

def f(a):
    if a != parent[a]:
        parent[a] = f(parent[a])
    return parent[a]

def u(a,b):
    rA,rB = f(a),f(b)
    if rA != rB:
        if rank[rA] > rank[rB]:
            parent[rB] = parent[rA]
        elif rank[rB] > rank[rA]:
            parent[rA] = parent[rB]
        else:
            parent[rB] = parent[rA]
            rank[rA]+=1
        return 0
    return 1

ans = 0
for i in range(m):
    a,b = map(int,input().split())
    if u(a,b):
        ans = i+1
        break

print(ans)