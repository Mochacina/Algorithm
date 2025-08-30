import sys

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

def dfs(x, y, visited, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(board[nx][ny]) - ord('A')
            if not (visited & (1 << idx)):  # 방문하지 않은 알파벳
                dfs(nx, ny, visited | (1 << idx), cnt + 1)

start = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, start, 1)
print(ans)