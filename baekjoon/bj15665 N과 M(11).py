n,m = map(int, input().split())
l = sorted(list(map(int,input().split())))
l2=[]
def dfs(s=[]):
    if len(s) == m:
        print(*s)
        return
    o = 0
    for i in range(n):
        if o != l[i]: 
            o = l[i]
            dfs(s+[l[i]])
dfs()