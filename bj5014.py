from collections import deque

def bfs():
    q = deque([S])
    visited = [0]*(F+1)
    while q:
        node = q.popleft()
        if node == G:
            print(visited)
            return visited[node]
        up = node+U
        down = node-D
        if up<=F and visited[up]==0:
            q.append(up)
            visited[up] = visited[node]+1
        if down>0 and visited[down]==0:
            q.append(down)
            visited[down] = visited[node]+1
    print(visited)
    return "use the stairs"

F,S,G,U,D = map(int, input().split())
print(bfs())
    