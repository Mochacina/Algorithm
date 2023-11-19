n,m = map(int, input().split())
l = sorted(list(map(int,input().split())))
l2=[]
v=[0]*n
def dfs(s=[]):
    if len(s) == m:
        t = ' '.join(map(str,s))
        if t not in l2:
            l2.append(t)
        return
    for i in range(n):
        if not v[i]:
            v[i]=1
            dfs(s+[l[i]])
            v[i]=0
dfs()
[print(i)for i in l2]