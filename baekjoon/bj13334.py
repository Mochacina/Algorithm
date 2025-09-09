import sys
import heapq

def solve():
    n = int(sys.stdin.readline())
    
    # 디버그 로그: 입력된 사람 수
    # print(f"DEBUG: 사람 수 n = {n}")

    locations = []
    for _ in range(n):
        h, o = map(int, sys.stdin.readline().split())
        # 시작점과 끝점을 정렬
        start, end = min(h, o), max(h, o)
        locations.append((start, end))

    d = int(sys.stdin.readline())
    
    # 디버그 로그: 철로 길이
    # print(f"DEBUG: 철로 길이 d = {d}")

    # 철로 길이보다 집-사무실 거리가 먼 경우는 제외
    valid_locations = []
    for start, end in locations:
        if end - start <= d:
            valid_locations.append((start, end))
    
    # 끝점을 기준으로 오름차순 정렬, 끝점이 같으면 시작점 기준 오름차순
    valid_locations.sort(key=lambda x: (x[1], x[0]))
    
    # 디버그 로그: 정렬된 유효 위치
    # print(f"DEBUG: 정렬된 유효 위치 = {valid_locations}")

    max_count = 0
    pq = []  # 최소 힙으로 사용할 우선순위 큐

    for start, end in valid_locations:
        # 현재 철로의 시작점
        rail_start = end - d
        
        # 현재 사람을 우선순위 큐에 추가 (시작점을 저장)
        heapq.heappush(pq, start)
        
        # 디버그 로그: push 후 pq 상태
        # print(f"DEBUG: {end}에서 push({start}), pq = {pq}")

        # 우선순위 큐에서 현재 철로의 범위를 벗어나는 것들을 제거
        while pq and pq[0] < rail_start:
            popped = heapq.heappop(pq)
            # 디버그 로그: pop 연산
            # print(f"DEBUG: {end}에서 rail_start({rail_start})보다 작은 {popped} pop, pq = {pq}")

        # 현재 철로에 포함된 사람 수로 최댓값 갱신
        current_count = len(pq)
        if current_count > max_count:
            max_count = current_count
            # 디버그 로그: 최댓값 갱신
            # print(f"DEBUG: 최댓값 갱신! max_count = {max_count}")

    print(max_count)

solve()