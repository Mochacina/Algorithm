import heapq

for _ in ' '*int(input()):
    n = int(input())
    l = map(int,input().split())
    hq = []
    for i in l: heapq.heappush(hq, i)
    for _ in range(n//2): heapq.heappop(hq)
    print(heapq.heappop(hq))