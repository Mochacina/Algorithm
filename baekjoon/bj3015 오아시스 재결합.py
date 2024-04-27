# l = [int(input()) for _ in range(int(input()))]
# s = []
# r = 0
# for i in l:
#     while s and s[-1][0] < i:
#         r += 1
#         s.pop()
#     if s and s[-1][0] == i:
#         t = s.pop()[1]
#         r += t
#         if s: r += 1
#         s.append((i, t + 1))
#     else:
#         s.append((i, 1))
#         if s: r += 1
# print(r)

l = [int(input()) for _ in range(int(input()))]
s = []
r = 0

for i in l:
    while s and s[-1][0] < i:
        r += s.pop()[1]
    if s and s[-1][0] == i:
        t = s.pop()[1]
        r += t
        if s: r += 1
        s.append((i, t+1))
    else:
        if s: r += 1
        s.append((i,1))
print(r)