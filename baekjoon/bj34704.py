import sys
from collections import Counter

data = list(map(int, sys.stdin.read().split()))
if not data:
    raise SystemExit
_, *arr = data

c = Counter(arr)
c1, c2, c3, c4 = c[1], c[2], c[3], c[4]

boxes = 0
boxes += c4

boxes += c3
c1 = max(0, c1 - c3)

boxes += c2 // 2
if c2 % 2:
    boxes += 1
    c1 = max(0, c1 - 2)

boxes += (c1 + 3) // 4

print(boxes)
