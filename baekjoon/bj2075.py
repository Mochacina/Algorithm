import heapq, sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    l = list(map(int,input().split()))
    for i in l:
        if len(hq)<n: heapq.heappush(hq, i)
        else:
            if i > hq[0]: heapq.heapreplace(hq,i)
print(hq[0])