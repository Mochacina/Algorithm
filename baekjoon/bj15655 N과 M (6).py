n,m=map(int,input().split())
l=sorted(list(map(int,input().split())))
def dfs(a,b,s):
 if b==m:print(*s)
 [dfs(i+1,b+1,s+[l[i]]) for i in range(a,n)]
dfs(0,0,[])

# def dfs(a):
#     if len(c) >=2:
#         if c[-2] > c[-1]: return
#     if len(c) >= m:
#         print(' '.join(map(str,c)));return
#     for i in range(a,n):
#         if l[i] not in c:
#             c.append(l[i])
#             dfs(a+1)
#             c.pop()
# dfs(0)
