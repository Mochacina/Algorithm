N = int(input())
l = [[] for _ in range(N+1)]
for i in range(1,N+1): 
    n = int(input())
    l[n].append(i)

ans = []
def dfs(start, i):
    v[i] = 1
    
    for n in l[i]:
        if n == start:
            ans.append(start)
            return
        elif v[n] == 0: dfs(start, n)

for i in range(1, N+1):
    v = [0]*(N+1)
    dfs(i,i)

ans.sort()
print(len(ans))
for a in ans: print(a)
