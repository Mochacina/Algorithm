import heapq, sys
input = sys.stdin.readline

min_heap = []
max_heap = []
entry_finder = {}
clients = {}

while c:=[*input().split()]:
    if c[0] == '0': exit()

    if c[0] == '1':
        client = int(c[1])
        pri = int(c[2])
        heapq.heappush(min_heap, pri)
        heapq.heappush(max_heap, -pri)
        entry_finder[pri] = entry_finder.get(pri, 0) + 1
        clients[pri] = client

    if c[0] == '2':
        # 최대 힙에서 최댓값 제거
        while max_heap and entry_finder[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        if max_heap:
            max_val = -heapq.heappop(max_heap)
            entry_finder[max_val] -= 1
            print(clients[max_val])
        else: print(0)
                
    if c[0] == '3':
        # 최소 힙에서 최솟값 제거
        while min_heap and entry_finder[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        if min_heap:
            min_val = heapq.heappop(min_heap)
            entry_finder[min_val] -= 1
            print(clients[min_val])
        else: print(0)

    # 유효하지 않은 값 제거
    while max_heap and entry_finder[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and entry_finder[min_heap[0]] == 0:
        heapq.heappop(min_heap)

# 결과 출력
# if not max_heap or not min_heap:
#     print("EMPTY")
# else:
#     print(-max_heap[0], min_heap[0])