from collections import deque
import sys

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
def bfs(n):
    v = [-1]*(N+1)
    q = deque([n])
    v[n] = 0
    
    while q:
        node = q.popleft()
        
        for n_node in arr[node]:
            if v[n_node] == -1:
                v[n_node] = v[node]+1
                q.append(n_node)
        
    return sum(v)
    
min_total = sys.maxsize
min_i = 0
for i in range(1, N+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        min_i = i
print(min_i)
        