from collections import deque

def solution():
    # 입력 받기
    K = int(input())  # 말처럼 이동할 수 있는 횟수
    W, H = map(int, input().split())  # 가로, 세로 크기
    grid = []
    for _ in range(H):
        row = list(map(int, input().split()))
        grid.append(row)
    
    horse_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    # 일반 이동 방향 (상하좌우)
    normal_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐 초기화
    # 상태: (행, 열, 남은 말 이동 횟수, 현재까지의 이동 횟수)
    queue = deque([(0, 0, K, 0)])
    
    # 방문 체크 배열 (3차원: 행, 열, 남은 말 이동 횟수)
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = True
    
    while queue:
        row, col, remaining_horse_moves, moves = queue.popleft()
        
        # 목표 지점 도달 확인
        if row == H - 1 and col == W - 1:
            return moves
        
        # 1. 말처럼 이동 (나이트 이동)
        if remaining_horse_moves > 0:
            for dr, dc in horse_moves:
                new_row, new_col = row + dr, col + dc
                
                # 범위 체크
                if 0 <= new_row < H and 0 <= new_col < W:
                    # 장애물이 아니고 방문하지 않은 경우
                    if grid[new_row][new_col] == 0 and not visited[new_row][new_col][remaining_horse_moves - 1]:
                        visited[new_row][new_col][remaining_horse_moves - 1] = True
                        queue.append((new_row, new_col, remaining_horse_moves - 1, moves + 1))
        
        # 2. 일반 이동 (상하좌우)
        for dr, dc in normal_moves:
            new_row, new_col = row + dr, col + dc
            
            # 범위 체크
            if 0 <= new_row < H and 0 <= new_col < W:
                # 장애물이 아니고 방문하지 않은 경우
                if grid[new_row][new_col] == 0 and not visited[new_row][new_col][remaining_horse_moves]:
                    visited[new_row][new_col][remaining_horse_moves] = True
                    queue.append((new_row, new_col, remaining_horse_moves, moves + 1))
    
    # 도달할 수 없는 경우
    return -1

# 메인 실행
if __name__ == "__main__":
    result = solution()
    print(result)