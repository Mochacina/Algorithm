n=int(input())
(l:=[*map(int, input().split())]).sort(key=lambda x: abs(x))
m=2e9
for i in range(n-1):
    for j in range(i+1, n):
        s = l[i]+l[j]
        if abs(s) < m:
            m = abs(s)
            a, b = l[i], l[j]
        else: break
print(*sorted([a, b]))