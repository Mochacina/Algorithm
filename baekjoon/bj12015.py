import bisect

n = int(input())
a = list(map(int, input().split()))

lis = []

for x in a:
    pos = bisect.bisect_left(lis, x)
    if pos == len(lis):
        lis.append(x)
    else:
        lis[pos] = x

print(len(lis))