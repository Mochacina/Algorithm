n,m=map(int,input().split())
l=sorted(list(map(int,input().split())))
c=[]
def dfs():
    if len(c)==m:
        print(' '.join(map(str,c)));return
    for i in range(n):
        if l[i] not in c:
            c.append(l[i])
            dfs()
            c.pop()
dfs()