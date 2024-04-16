# import sys 
# sys.setrecursionlimit(10**5)
# n,m = map(int,input().split())
# l = [i for i in range(n+1)]
# def union(a,b):
#     xa = find(a)
#     xb = find(b)
#     l[xb] = xa
# def find(a):
#     if a != l[a]:
#         l[a] = find(l[a])
#     return l[a]
# for _ in range(m):
#     n,a,b = map(int,input().split())
#     if n: print(['NO','YES'][find(a)==find(b)])
#     else: union(a,b)

n,m = map(int,input().split())
li = [i for i in range(n+1)]
def finder(a):
    if a!=li[a]:
        li[a] = finder(li[a])
    return li[a]
for _ in range(m):
    n,a,b = map(int,input().split())
    if n: print(['NO','YES'][finder(a)==finder(b)])
    else:
        l = finder(a)
        r = finder(b)
        li[r] = l