import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    row_k = graph[k]
    for i in range(N):
        if graph[i][k]:
            for j in range(N):
                if row_k[j]:
                    graph[i][j] = 1

for i in range(N):
    print(' '.join(map(str, graph[i])))