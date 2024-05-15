import heapq
n,k=map(int,input().split())
j=sorted([[*map(int,input().split())]for _ in range(n)])
b=sorted([int(input())for _ in range(k)])
hq=[]
j_idx=0
score=0

for bag in b:
    while j_idx < n and j[j_idx][0] <= bag:
        heapq.heappush(hq, -j[j_idx][1])
        j_idx += 1
    if hq:
        score -= heapq.heappop(hq)
        
print(score)