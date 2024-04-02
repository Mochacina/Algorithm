K, N = map(int, input().split())
l = [int(input()) for _ in range(K)]
start, end = 1, max(l)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in l:
        cnt += i // mid
    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)