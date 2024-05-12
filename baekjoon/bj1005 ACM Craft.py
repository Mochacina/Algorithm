from collections import deque

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    arr = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X].append(Y)
        degree[Y] += 1

    W = int(input())

    q = deque()
    time = [0] * (N + 1)

    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
            time[i] = D[i]

    while q:
        idx = q.popleft()

        for a in arr[idx]:
            degree[a] -= 1
            time[a] = max(time[idx] + D[a], time[a])
            if degree[a] == 0:
                q.append(a)

        if idx == W: break

    print(time[W])
