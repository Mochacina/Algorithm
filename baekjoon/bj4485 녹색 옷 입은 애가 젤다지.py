import heapq

di = [(0,1),(1,0),(-1,0),(0,-1)]

p = 0
while n := int(input()):
    p+=1
    l = [[*map(int, input().split())] for _ in range(n)]
    cost_map = [[float("INF")]*n for _ in range(n)]
    
    q = [(l[0][0],(0,0))]
    cost_map[0][0] = l[0][0]
    while q:
        co, node = heapq.heappop(q)
        x,y = node
        
        if co > cost_map[x][y]: continue
        for dx, dy in di:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                dcost = l[nx][ny]
                cost = dcost + co
                if cost < cost_map[nx][ny]:
                    cost_map[nx][ny] = cost
                    heapq.heappush(q, (cost,(nx,ny)))

    print(f"Problem {p}: {cost_map[-1][-1]}")