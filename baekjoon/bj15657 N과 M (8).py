n,m = map(int, input().split())
l = sorted(list(map(int,input().split())))
def dfs(a,s=[]):
    if len(s) >= m:
        print(' '.join(map(str,s)));return
    for i in range(a,n):
        dfs(i,s+[l[i]])
dfs(0)
