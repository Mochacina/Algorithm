import heapq, sys

input = sys.stdin.readline

for _ in ' '*int(input()):
    mnHq = []
    mxHq = []
    entry_finder = {}
    
    for _ in ' '*int(input()):
        i, v = input().split()
        v = int(v)
        if i == 'I':
            heapq.heappush(mnHq, v)
            heapq.heappush(mxHq, -v)
            entry_finder[v] = entry_finder.get(v, 0) + 1
        elif i == 'D':
            if v == 1:
                while mxHq and entry_finder[-mxHq[0]] == 0:
                    heapq.heappop(mxHq)
                if mxHq:
                    p = -heapq.heappop(mxHq)
                    entry_finder[p] -= 1
            else:
                while mnHq and entry_finder[mnHq[0]] == 0:
                    heapq.heappop(mnHq)
                if mnHq:
                    p = heapq.heappop(mnHq)
                    entry_finder[p] -= 1
                
    if not len(mnHq): print("EMPTY")
    else:
        print(-heapq.heappop(mxHq), heapq.heappop(mnHq))