# n = int(input())
# l = sorted([*map(int,input().split())])
# m = [0]*(max(l)+1)
# x = int(input())
# s = set()
# for i in l:m[i] = 1
# for i in l:
#     if m[x-i]:
#         mi,ma = min(i,x-i),max(i,x-i)
#         s.add((mi,ma))
# print(len(s))

n = int(input())
l = sorted(map(int, input().split()))
x = int(input())

i, j = 0, n - 1
cnt = 0
while i < j:
    s = l[i] + l[j]
    if s == x:
        cnt += 1
        i += 1
        j -= 1
    elif s < x:
        i += 1
    else:
        j -= 1

print(cnt)