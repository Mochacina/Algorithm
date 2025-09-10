import sys
import heapq

input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    h,o = map(int,input().split())
    s,e = min(h,o), max(h,o)
    l.append((s,e))

d = int(input())
valid_l = []
for s,e in l:
    if e-s <= d:
        valid_l.append((s,e))

valid_l.sort(key=lambda x: (x[1],x[0]))
max_cnt = 0
pq = []

for s,e in valid_l:
    rail_start = e - d
    heapq.heappush(pq, s)
    
    while pq and pq[0] < rail_start:
        popped = heapq.heappop(pq)
    
    current_count = len(pq)
    if current_count > max_cnt:
        max_cnt = current_count

print(max_cnt)
    