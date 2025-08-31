import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸과 바이러스 좌표 저장
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(lab_map):
    """바이러스 퍼뜨린 후 남은 안전 영역 크기 계산"""
    q = deque(virus)
    visited = [[False]*M for _ in range(N)]
    
    for x, y in virus:
        visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if lab_map[nx][ny] == 0 and not visited[nx][ny]:
                    lab_map[nx][ny] = 2
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    # 안전 영역 세기
    safe = sum(row.count(0) for row in lab_map)
    return safe

ans = 0
# 빈 칸에서 3개를 골라 벽을 세움
for walls in combinations(empty, 3):
    # 연구소 복사
    lab_copy = [row[:] for row in lab]
    # 벽 세우기
    for x, y in walls:
        lab_copy[x][y] = 1
    # 바이러스 퍼뜨리고 안전 영역 계산
    ans = max(ans, spread(lab_copy))

print(ans)