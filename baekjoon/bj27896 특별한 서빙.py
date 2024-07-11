import heapq

def min_eggplants_to_avoid_protest(N, M, dissatisfaction):
    current_dissatisfaction = 0
    eggplants_needed = 0
    max_heap = []
    
    for i in range(N):
        current_dissatisfaction += dissatisfaction[i]
        heapq.heappush(max_heap, -dissatisfaction[i])
        
        while current_dissatisfaction >= M:
            largest_dissatisfaction = -heapq.heappop(max_heap)
            current_dissatisfaction -= 2 * largest_dissatisfaction
            eggplants_needed += 1
    
    return eggplants_needed

N, M = map(int, input().split())
dissatisfaction = list(map(int, input().split()))
print(min_eggplants_to_avoid_protest(N, M, dissatisfaction))