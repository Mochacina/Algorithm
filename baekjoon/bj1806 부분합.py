n,s = map(int, input().split())
li = [*map(int, input().split())]
l, r, res, cSum = 0, 0, 100001, 0
while r <= n:
    if s > cSum:
        if r < n: cSum += li[r]
        r += 1
    else:
        res = min(res, r-l)
        cSum -= li[l]
        l += 1
print(res if res != 100001 else 0)