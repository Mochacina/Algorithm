N, K = map(int, input().split())
A = [*map(int, input().split())]
robot = [0] * N
cnt = 0
while A.count(0) < K:
    cnt += 1
    A = [A[-1]] + A[:-1]
    robot = [robot[-1]] + robot[:-1]
    robot[-1] = 0
    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and A[i + 1]:
            robot[i] = 0
            robot[i + 1] = 1
            A[i + 1] -= 1
    robot[-1] = 0
    if A[0]:
        robot[0] = 1
        A[0] -= 1
print(cnt)