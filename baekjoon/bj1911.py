import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pools = [tuple(map(int, input().split())) for _ in range(N)]
pools.sort()  # 시작 기준 오름차순

covered = 0
ans = 0
for s, e in pools:
    if covered >= e:
        continue
    start = max(s, covered)
    rem = e - start
    k = (rem + L - 1) // L
    ans += k
    covered = start + k * L

print(ans)