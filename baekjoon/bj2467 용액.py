# sort by abs
# n=int(input())
# (l:=[*map(int, input().split())]).sort(key=lambda x: abs(x))
# m=2e9
# for i in range(n-1):
#     for j in range(i+1, n):
#         s = l[i]+l[j]
#         if abs(s) < m:
#             m = abs(s)
#             a, b = l[i], l[j]
#         else: break
# print(*sorted([a, b]))

# two pointers 1
# n = int(input())
# arr = list(map(int, input().split()))

# l,r = 0,n-1
# m = 2e9
# pair = (arr[l], arr[r])

# while l < r:
#     sxm = arr[l] + arr[r]
#     if abs(sxm) < abs(m):
#         m = sxm
#         pair = (arr[l], arr[r])
    
#     if sxm < 0: l += 1
#     else: r -= 1

# print(*sorted(pair))

# two pointers 2
n = int(input())
li = [*map(int, input().split())]
l,r = 0,n-1
m = 2e9
pair = [li[l],li[r]]
while l < r:
    s = li[l] + li[r]
    if abs(s) < abs(m):
        m = s
        pair = [li[l],li[r]]
    if s < 0: l+=1
    else: r-=1
print(*pair)