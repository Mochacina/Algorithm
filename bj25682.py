def get_min(M, N, K, grid):
    prefix_sums = [[0] * (N + 1) for _ in range(M + 1)]

    # 누적합 계산
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            prefix_sums[i][j] = prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1]
            if (i + j) % 2 == 0:
                if grid[i-1][j-1] == 'W':
                    prefix_sums[i][j] += 1
            else:
                if grid[i-1][j-1] == 'B':
                    prefix_sums[i][j] += 1

    print(prefix_sums)
    mcnt = float('inf')

    for i in range(K, M + 1):
        for j in range(K, N + 1):
            count = prefix_sums[i][j] - prefix_sums[i-K][j] - prefix_sums[i][j-K] + prefix_sums[i-K][j-K]
            mcnt = min(mcnt, count, K*K - count)

    return mcnt

M, N, K = map(int, input().split())
grid = []
for _ in range(M):
    row = input()
    grid.append([row[i] for i in range(N)])

min = get_min(M, N, K, grid)
print(min)