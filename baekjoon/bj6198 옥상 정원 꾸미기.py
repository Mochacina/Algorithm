l = [int(input()) for _ in range(int(input()))]
s = []
r = 0

for i in range(len(l)):
    while s and s[-1][0] <= l[i]:
        s.pop()
    r += len(s)
    s.append((l[i], i))
    
print(r)