n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    if coin <= k:  # k보다 큰 동전은 사용할 필요가 없음
        coins.append(coin)

# dp[i]는 금액 i를 만드는 데 필요한 최소 동전 개수
dp = [0] + [float('inf')]*k

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != float('inf'):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != float('inf') else -1)

# if dp[k] == float('inf'):
#     print(-1)  # k원을 만드는 것이 불가능한 경우
# else:
#     print(dp[k])
