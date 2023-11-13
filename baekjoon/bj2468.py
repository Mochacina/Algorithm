# from collections import deque

# di = [(-1,0),(1,0),(0,-1),(0,1)]
# def bfs(depth,a,b):
#     visited[a][b] = 1
#     count = 1
#     queue = deque([(a,b)])
    
#     while queue:
#         xy = queue.popleft()
#         for i in di:
#             nx = xy[0]+i[0]
#             ny = xy[1]+i[1]
#             if nx<0 or ny<0 or nx>=n or ny>=n: continue
#             if visited[nx][ny] == 0 and l[nx][ny] > depth:
#                 visited[nx][ny] = 1
#                 queue.append((nx,ny))
#                 count += 1
#     return count

# l = []
# n = int(input())
# visited = []
# for _ in range(n): l.append(list(map(int,input().split())))

# maxN = max([max(i) for i in l])
# op = [[] for _ in range(maxN)]
# for k in range(maxN):
#     visited = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n): 
#             if l[i][j] > k and not visited[i][j]: 
#                 op[k-1].append(bfs(k,i,j))

# print(max([len(i) for i in op]))

from collections import deque

di = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(depth,a,b):
    visited[a][b] = 1
    queue = deque([(a,b)])
    
    while queue:
        x,y = queue.popleft()
        for i in di:
            nx = x+i[0]
            ny = y+i[1]
            if not (nx<0 or ny<0 or nx>=n or ny>=n):
                if visited[nx][ny] == 0 and l[nx][ny] > depth:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    return 1

l = []
n = int(input())
visited = []
for _ in range(n): l.append(list(map(int,input().split())))

maxN = max([max(i) for i in l])
op = [0]*maxN
for k in range(maxN):
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n): 
            if l[i][j] > k and not visited[i][j]: 
                op[k-1] += bfs(k,i,j)
print(max(op))