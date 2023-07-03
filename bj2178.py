from collections import deque

def bfs(maze, start):
    n = len(maze)
    m = len(maze[0])
    di = [(-1,0),(1,0),(0,-1),(0,1)]
    
    queue = deque([(start, 1)]) 
    visited = [[False]*m for _ in range(n)]
    
    while queue:
        xy, count = queue.popleft()
        print(xy, count)
        if xy[0] == n-1 and xy[1] == m-1: return count
        
        for i in di:
            nx = xy[0]+i[0]
            ny = xy[1]+i[1]
            
            if (0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1
                    and not visited[nx][ny]):
                queue.append(((nx, ny), count+1))
                visited[nx][ny] = True
    

n,m = map(int, input().split())
l = [list(map(int, input())) for _ in range(n)]
zp = [0,0]
    
print(bfs(l,zp))