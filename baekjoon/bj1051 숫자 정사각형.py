def find_squre(s):
    for i in range(0,N-s+1):
        for j in range(0,M-s+1):
            if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return 1
    return 0

N, M = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(N)]

for k in range(min(N,M), 0, -1):
    if find_squre(k):
        print(k**2)
        break