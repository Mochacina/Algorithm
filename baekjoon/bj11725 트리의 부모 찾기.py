# import sys
# sys.setrecursionlimit(10**6)
# n = int(input())
# l = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a,b = map(int,input().split())
#     l[a].append(b)
#     l[b].append(a)
# v = [0]*(n+1)
# def dfs(n):
#     for i in l[n]:
#         if not v[i]:
#             v[i] = n
#             dfs(i)
# dfs(1)
# for i in range(2,n+1):
#     print(v[i])

from collections import deque
n = int(input())
l = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
v = [0]*(n+1)
deq = deque([1])
def bfs():
    while deq:
        n = deq.popleft()
        for i in l[n]:
            if not v[i]:
                v[i] = n
                deq.append(i)
bfs()
for i in range(2,n+1):
    print(v[i])