# n,m = map(int, input().split())
# l = sorted(list(map(int,input().split())))
# l2=[]
# v=[0]*n
# def dfs(s=[]):
#     if len(s) == m:
#         if set(s) not in l2:
#             l2.append(set(s))
#             print(' '.join(map(str,s)))
#         return
#     for i in range(n):
#         if not v[i]:
#             v[i]=1
#             dfs(s+[l[i]])
#             v[i]=0
# dfs()


n,m = map(int, input().split())
l = sorted(list(map(int,input().split())))
l2=[]
v=[0]*n
def dfs(a,s=[]):
    if len(s) == m:
        t = ' '.join(map(str,s))
        if t not in l2:
            l2.append(t)
        return
    for i in range(a,n):
        if not v[i]:
            v[i]=1
            dfs(i+1,s+[l[i]])
            v[i]=0
dfs(0)
[print(i)for i in l2]