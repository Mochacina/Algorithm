import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 테트로미노 19가지 모양
shapes = [
    # ㅡ, ㅣ
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],

    # ㅁ
    [(0,0),(0,1),(1,0),(1,1)],

    # L, J 형태
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,2),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,1),(1,1),(2,0),(2,1)],
    [(0,0),(0,1),(0,2),(1,2)],

    # Z, S 형태
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(1,0),(1,-1),(2,-1)],
    [(0,0),(0,1),(1,1),(1,2)],

    # ㅗ 형태
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,1),(1,0),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(1,1)],
]

answer = 0

for i in range(N):
    for j in range(M):
        for shape in shapes:
            try:
                s = 0
                for dx, dy in shape:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        raise IndexError
                    s += board[nx][ny]
                answer = max(answer, s)
            except IndexError:
                continue

print(answer)