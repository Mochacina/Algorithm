# import sys
# input = sys.stdin.readline
# n = int(input())
# l = [int(input()) for _ in range(n)]
# #print(l)
# ans = ['']
# def bt(a,s=''):
#     if a >= n:
#         if len(s) >= len(ans[-1]):ans.append(s)
#         return
#     if len(s)==0:bt(a+1,s+str(l[a]))
#     elif len(s)==1:
#         if int(s[-1]) != l[a]: bt(a+1,s+str(l[a]))
#     else:
#         if int(s[-2]) < int(s[-1]):
#             if int(s[-1]) > l[a]: bt(a+1,s+str(l[a]))
#         elif int(s[-2]) > int(s[-1]):
#             if int(s[-1]) < l[a]: bt(a+1,s+str(l[a]))
#     bt(a+1,s)
# bt(0)
# print(len(ans[-1]))

import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]

up = [1] * n
down = [1] * n

for i in range(1, n):
    if l[i] > l[i-1]:
        up[i] = down[i-1] + 1
        down[i] = down[i-1]
    elif l[i] < l[i-1]:
        down[i] = up[i-1] + 1
        up[i] = up[i-1]
    else:
        up[i] = up[i-1]
        down[i] = down[i-1]
            
print(max(up[n-1], down[n-1]))