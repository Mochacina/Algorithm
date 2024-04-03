N = int(input())
l = [*map(int, input().split())]
cum_sum = [0]*N
sum = 0
for i in range(N):
    sum += l[i]
    cum_sum[i] = sum
ans = 0
for i in range(1, N-1):
    sum1 = cum_sum[i-1] + cum_sum[N-2] - l[i] # 벌통이 0
    sum2 = cum_sum[i] + cum_sum[N-2] - l[0] - cum_sum[i-1] # 벌통이 i
    sum3 = cum_sum[N-1]*2 - cum_sum[i] - l[0] - l[i] # 벌통이 N-1
    ans = max(ans, max(sum1,sum2,sum3))
print(ans)
