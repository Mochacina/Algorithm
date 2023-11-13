import sys
input = sys.stdin.readline
d = {}
a,b = map(int,input().split())
for _ in range(a):
    n = input().rstrip()
    if(len(n)>=b):
        if(d.get(n)==None):d[n]=1
        else:d[n]=d[n]+1
d = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in d:print(i[0])

# try:
#     for i in range(max(d.values()),0,-1):
#         l = [k for k,v in d.items() if v==i]
#         for j in range(max([len(le) for le in l]),0,-1):
#             l2 = [k2 for k2 in l if len(k2)==j]
#             l2 = sorted(l2)
#             for word in l2:
#                 print(word)
# except:
#     exit()