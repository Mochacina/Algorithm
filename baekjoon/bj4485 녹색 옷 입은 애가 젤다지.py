import heapq

di = [(0,1),(1,0),(-1,0),(0,-1)]

p = 0
while n := int(input()):
    p+=1
    l = [[*map(int, input().split())] for _ in range(n)]
    cost_map = [[float("INF")]*n for _ in range(n)]
    
    q = [(0,0,0)]
    cost_map[0][0] = l[0][0]
    while q:
        co,x,y = heapq.heappop(q)
        
        if co > cost_map[x][y]: continue
        for dx, dy in di:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = l[nx][ny]
                cost = next_cost + cost_map[x][y]
                if cost < cost_map[nx][ny]:
                    cost_map[nx][ny] = cost
                    heapq.heappush(q, (cost,nx,ny))

    print(f"Problem {p}: {cost_map[-1][-1]}")