# n = int(input())
# l = [*map(int, input().split())]
# cnt = 0
# for i in range(n-1):
#     #print(l)
#     if l[i] and l[i+1]:
#         m = min(l[i], l[i+1])
#         l[i] -= m; l[i+1] -= m
#         cnt += 1
# #print(l)
# for i in l:
#     if i: cnt+=1
# print(min(cnt, n))

# n = int(input())
# l = [*map(int, input().split())]
# cnt = 0
# for i in range(n-1):
#     if l[i] and l[i+1]:
#         if l[i] > l[i+1]:
#             l[i] = 0
#             cnt += 1
#         else:
#             m = min(l[i], l[i+1])
#             l[i] -= m; l[i+1] -= m
#             cnt += 1
# if l[-1]: cnt+=1
# print(min(cnt, n))

# N = int(input())
# stone = list(map(int, input().split()))
# stone_cnt = stone[:]
# cnt = N
# for i in range(1, N):
#    for sc in stone_cnt[i-1]:
#       if sc < stone[i]:
#          stone_cnt[i].append(stone[i] - sc)
#       elif sc == stone[i]:
#          stone_cnt[i] = []
#          cnt -= 1
#          break
# print(cnt)

# N = int(input())
# stone = list(map(int, input().split()))

# rStone = [[i] for i in stone]
# cnt = N

# for i in range(1, N):
#     #print(stone, rStone)
#     for rs in rStone[i-1]:
#         if rs < stone[i]:
#             rStone[i].append(stone[i] - rs)
#         elif rs == stone[i]:
#             rStone[i] = []
#             cnt -= 1
#             break
# print(cnt)

# N = int(input())
# rock = [*map(int,input().split())]
# DP = [0]*N
# for i in range(N):
#   DP[i] = max(DP[i],DP[i-1])
#   x = rock[i]
#   for j in range(i+1,N):
#     x = rock[j]-x
#     if x<0: break
#     if x==0:
#       DP[j] = max(DP[j],DP[i-1]+1)
#       break
#   print(DP)
# print(N-DP[-1])

N=int(input())
l=[*map(int,input().split())]
c=[0]*N
for i in range(N):
 c[i]=max(c[i],c[i-1])
 n=l[i]
 for j in range(i+1,N):
  n=l[j]-n
  if n<0:break
  if n==0:c[j]=max(c[j],c[i-1]+1);break
print(N-c[-1])

# N = int(input())
# l = [*map(int, input().split())]
# cnt = [0]*N
# for i in range(N-1):
#     n = l[i]
#     for j in range(i+1, N):
#         if n > l[j]: break
#         elif n == l[j]:
#             cnt[i] += 1
#             break
#         elif n < l[j]:
#             n = l[j]-n
# print(cnt)
# print(N-sum(cnt))

# N = int(input())
# l = [*map(int, input().split())]
# cnt = [0]*N
# for i in range(N-1):
#     n = l[i]
#     j = i+1
#     while j < N:
#         if n > l[j]: break
#         elif n == l[j]:
#             cnt[i] += 1
#             if j < N-2:
#                 j+=1
#                 n=l[j]
#         elif n < l[j]:
#             n = l[j]-n
#         j+=1
# print(N-max(cnt))