import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    qst = int(input())
    if qst: heapq.heappush(heap, qst)
    else:
        if len(heap):
            temp = heapq.heappop(heap)
            print(temp)
        else: print(0)