n,m,k = map(int,input().split())
candies = [0]+[*map(int,input().split())]
graph = [[] for _ in range(n+1)]
vi = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
l = []
def find_friends(i):
    w,v = 1,candies[i]
    vi[i] = 1
    q = [i]
    while q:
        node = q.pop()
        for n_node in graph[node]:
            if not vi[n_node]:
                q.append(n_node)
                w,v = w+1,v+candies[n_node]
                vi[n_node] = 1
    l.append((w,v))
for i in range(1,n+1):
    if not vi[i]: find_friends(i)
dp = [0]*(k)
for w,v in l:
    for j in range(k-1,w-1,-1):
        dp[j]=max(dp[j],dp[j-w]+v)
print(dp[-1])