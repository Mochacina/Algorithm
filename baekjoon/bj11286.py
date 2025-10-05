import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    qu = int(input())
    if qu: heapq.heappush(heap, (abs(qu), qu))
    else:
        if len(heap):
            q1,q2 = heapq.heappop(heap)
            print(q2)
        else: print(0)