from collections import deque

N, K = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX + 1)
dq = deque()

dq.append(N)
visited[N] = 0

while dq:
    x = dq.popleft()
    
    if x == K:
        print(visited[x])
        break

    if 0 <= 2*x <= MAX and visited[2*x] == -1:
        visited[2*x] = visited[x]
        dq.appendleft(2*x)

    for nx in (x-1, x+1):
        if 0 <= nx <= MAX and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            dq.append(nx)