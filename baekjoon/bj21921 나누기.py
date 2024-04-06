N, X = map(int, input().split())
arr = list(map(int, input().split()))
sw = sum(arr[:X])
max_sum = sw
max_cnt = 1

for i in range(X, N):
    sw -= arr[i - X]
    sw += arr[i]
    if sw == max_sum:
        max_cnt += 1
    elif max_sum < sw:
        max_sum = sw
        max_cnt = 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_cnt)