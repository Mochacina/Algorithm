from collections import deque

def bfs (graph, a,b):
    di = [(-1,0),(1,0),(0,-1),(0,1)]
    l[a][b] = 0
    count = 1
    queue = deque([(a,b)])
    
    while queue:
        xy = queue.popleft()
        for i in di:
            nx = xy[0]+i[0]
            ny = xy[1]+i[1]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if l[nx][ny] == 1:
                l[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count
    

n = int(input())
l = [list(map(int, input())) for _ in range(n)]

op = []
for i in range(n):
    for j in range(n): 
        if l[i][j] == 1: 
            op.append(bfs(l,i,j))

print(len(op))
for i in sorted(op): print(i)