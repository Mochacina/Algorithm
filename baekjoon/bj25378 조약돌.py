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

N = int(input())
stone = list(map(int, input().split()))

rStone = [[i] for i in stone]
cnt = N

for i in range(1, N):
    #print(stone, rStone)
    for rs in rStone[i-1]:
        if rs < stone[i]:
            rStone[i].append(stone[i] - rs)
        elif rs == stone[i]:
            rStone[i] = []
            cnt -= 1
            break
print(cnt)