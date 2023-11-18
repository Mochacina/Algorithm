import sys
N,M,B = map(int,input().split())
l = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
answer = sys.maxsize
idx = 0

for floor in range(257):
    pb, mb = 0, 0

    for i in range(N):
        for j in range(M):
            if l[i][j] > floor :
                pb += l[i][j] - floor
            else : 
                mb += floor - l[i][j]

    if pb + B >= mb :
        if (pb * 2) + mb <= answer:
            answer = (pb * 2) + mb
            idx = floor


print(answer, idx)