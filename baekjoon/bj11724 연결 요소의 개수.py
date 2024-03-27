N,M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
v = [0]*(N+1)
def dfs(n):
    v[n] = 1
    for i in G[n]:
        if not v[i]:
            dfs(i)
cnt = 0
for i in range(1,N+1):
    if not v[i]:
        cnt+=1
        dfs(i)
print(cnt)