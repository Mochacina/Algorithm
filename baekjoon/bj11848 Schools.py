import heapq
n,m,s = map(int,input().split())
hq_m, hq_s = [],[]
heapq.heapify(hq_m)
heapq.heapify(hq_s)
for i in range(n):
    a,b = map(int,input().split())
    dif = a-b
    heapq.heappush(hq_m,(-a,a,dif,i))
    heapq.heappush(hq_s,(-b,b,-dif,i))
