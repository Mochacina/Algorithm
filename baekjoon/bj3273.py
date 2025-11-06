n = int(input())
l = sorted([*map(int,input().split())])
x = int(input())
mx = max(max(l),x)
m = [0]*(mx+1)
cnt = 0
for i in l:
    nd = x-i
    if 0 <= nd <= mx and m[nd]: cnt+=1
    m[i] = 1
print(cnt)

# n = int(input())
# l = sorted(map(int, input().split()))
# x = int(input())

# i, j = 0, n - 1
# cnt = 0
# while i < j:
#     s = l[i] + l[j]
#     if s == x:
#         cnt += 1
#         i += 1
#         j -= 1
#     elif s < x:
#         i += 1
#     else:
#         j -= 1

# print(cnt)