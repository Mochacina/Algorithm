n = int(input())
l = [0]+[int(input()) for _ in range(n)]+[0]
s = [0]
m = 0
for i in range(1,n+2):
    while s and l[s[-1]] > l[i]:
        print(s) # 디버깅용 스택 출력
        num = s.pop()
        m = max(m,(i-s[-1]-1)*l[num])
    s.append(i)
print(m)

# n = int(input())
# l = [int(input()) for _ in range(n)] + [0]
# s = []
# m = 0
# for i in range(n + 1):
#     while s and s[-1][0] > l[i]:
#         hei, num = s.pop()
#         m = max(m, hei * (i - num))
#     s.append((l[i], i if not s else s[-1][1] if s[-1][0] == l[i] else i))
# print(m)