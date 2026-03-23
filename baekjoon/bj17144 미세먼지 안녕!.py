# r,c,t=map(int,input().split())
# l = []
# air_top = 0
# air_bottom = 0
# next_air = set()
# for i in range(r):
#     l2 = [*map(int,input().split())]
#     for j in range(c):
#         if l2[j] > 0: next_air.add((i,j))
#     l.append(l2) 
#     if not air_top and l[0] == -1:
#         air_top = i
#         air_bottom = i+1
# for _ in range(t):
#     pass
# print(next_air)
# print(sum([sum(l2) for l2 in l])+2)

r,c,t=map(int,input().split())
l = []
air_top = 0
air_bottom = 0

for i in range(r):
    l2 = [*map(int,input().split())]
    l.append(l2)
    if l2[0] == -1:
        if air_top == 0:
            air_top = i
            air_bottom = i+1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    # 1. 확산
    temp = [[0]*c for _ in range(r)]
    temp[air_top][0] = -1
    temp[air_bottom][0] = -1

    for i in range(r):
        for j in range(c):
            if l[i][j] > 0:
                spread = l[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0<=ni<r and 0<=nj<c and l[ni][nj] != -1:
                        temp[ni][nj] += spread
                        cnt += 1
                temp[i][j] += l[i][j] - spread*cnt

    l = temp

    # 2. 공기청정기 (위: 반시계)
    # 위쪽
    for i in range(air_top-1,0,-1):
        l[i][0] = l[i-1][0]
    for j in range(c-1):
        l[0][j] = l[0][j+1]
    for i in range(air_top):
        l[i][c-1] = l[i+1][c-1]
    for j in range(c-1,1,-1):
        l[air_top][j] = l[air_top][j-1]
    l[air_top][1] = 0

    # 아래쪽 (시계)
    for i in range(air_bottom+1,r-1):
        l[i][0] = l[i+1][0]
    for j in range(c-1):
        l[r-1][j] = l[r-1][j+1]
    for i in range(r-1,air_bottom,-1):
        l[i][c-1] = l[i-1][c-1]
    for j in range(c-1,1,-1):
        l[air_bottom][j] = l[air_bottom][j-1]
    l[air_bottom][1] = 0

print(sum([sum(row) for row in l]) + 2)