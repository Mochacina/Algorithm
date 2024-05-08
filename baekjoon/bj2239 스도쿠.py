N = 9
arr = [list(map(int, list(input()))) for _ in range(N)]
zero = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 0]

def is_possible(y, x, n):
    for i in range(9):
        if arr[y][i] == n:
            return 0
        if arr[i][x] == n:
            return 0

    ny = (y // 3) * 3
    nx = (x // 3) * 3

    for dy in range(3):
        for dx in range(3):
            if arr[ny + dy][nx + dx] == n:
                return 0
    return 1

def dfs(idx):
    if idx == len(zero):
        for row in arr:
            print(*row, sep='')
        exit(0)

    y, x = zero[idx]
    for i in range(1, 10):
        if is_possible(y, x, i):
            arr[y][x] = i
            dfs(idx + 1)
            arr[y][x] = 0
dfs(0)