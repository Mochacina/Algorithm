n,s = map(int, input().split())
li = [*map(int, input().split())]
l, r, res = 0, 0, 100001
while r <= n:
    if s <= sum(li[l:r]):
        res = min(res, r-l)
        l += 1
    else:
        r += 1
print(res if res != 100001 else 0)