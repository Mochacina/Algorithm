import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)