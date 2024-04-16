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

import sys
n,m = map(int,input().split())
li = [i for i in range(n+1)]
def f(a):
    if a!=li[a]: li[a] = f(li[a])
    return li[a]
for _ in range(m):
    n,a,b = map(int, sys.stdin.readline().split())
    if n: print(['NO','YES'][f(a)==f(b)])
    else:
        l,r = f(a),f(b)
        li[r] = l