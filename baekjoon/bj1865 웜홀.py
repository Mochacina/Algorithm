def bf():
    for t in range(n):
        for i in range(1,n+1):
            for next, w in nodes[i]:
                if dis[i]+w < dis[next]:
                    if t==n-1: return 1
                    dis[next] = dis[i]+w
    return 0

for _ in ' '*int(input()):
    n,m,w = map(int,input().split())
    nodes = [[] for _ in range(n+1)]
    for i in range(m+w):
        s,e,t = map(int, input().split())
        if i < m:
            nodes[s].append((e,t))
            nodes[e].append((s,t))
        else:
            nodes[s].append((e,-t))
    
    dis = [9e9]*(n+1)
    dis[1] = 0
    
    print(['NO','YES'][bf()])