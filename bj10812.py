n, m = map(int, input().split())
l = [i+1 for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    l2 = l[c-1:b]+l[a-1:c-1]
    for x, i in enumerate(range(a-1,b)): l[i] = l2[x]
print(*l)