n = int(input())
INF = float('inf')
cost = [[*map(int, input().split())] for _ in range(n)]

dp = [[INF] * n for _ in range(1 << n)]
for mask in range (1<<n):
    for i in range(n):
        if dp[mask][i] == INF:
            continue
        for j in range(n):
            if mask & (1 << j) or cost[i][j] == 0:
                continue
            next_mask = mask | (1 << j)
            dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + cost[i][j])

# 모든 도시를 방문한 상태에서 0번 도시로 돌아가는 비용 계산
final_mask = (1 << n) - 1
min_cost = INF
for i in range(1, n):
    if cost[i][0] > 0:
        min_cost = min(min_cost, dp[final_mask][i] + cost[i][0])