import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().strip())
S = list(map(int, input().split()))

left = 0
count = defaultdict(int)
max_len = 0

for right in range(N):
    count[S[right]] += 1

    while len(count) > 2:
        count[S[left]] -= 1
        if count[S[left]] == 0:
            del count[S[left]]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
