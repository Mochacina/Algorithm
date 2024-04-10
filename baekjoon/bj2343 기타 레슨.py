N, M = map(int, input().split())
l = list(map(int, input().split()))
s, e = max(l), sum(l)
while s <= e:
    m = (s+e)//2
    cnt, sum_ = 1, 0
    for i in l:
        if sum_ + i > m:
            cnt += 1
            sum_ = 0
        sum_ += i
    if cnt > M: s = m + 1
    else: e = m - 1
print(s)