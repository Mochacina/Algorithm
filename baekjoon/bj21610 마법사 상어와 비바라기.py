# N,M = map(int,input().split())
# L = [[*map(int,input().split())] for _ in range(N)]
# M = [[*map(int,input().split())] for _ in range(M)]
# d = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]] # x y
# rainClouds = [[0,N-1],[1,N-1],[0,N-2],[1,N-2]] # x y
# print(rainClouds)
# for i in M:
#     a,b = i
#     for j in range(len(rainClouds)):
#         rainClouds[j][0] = (rainClouds[j][0]+d[a-1][0]*b)%N
#         rainClouds[j][1] = (rainClouds[j][1]+d[a-1][1]*b)%N
#         L[rainClouds[j][1]][rainClouds[j][0]] += 1
#     print("rainClouds: ", rainClouds)
#     print("L: ")
#     for l in L:
#         print(l)
#     new_L = L.copy()
#     for j in range(len(rainClouds)):
#         x,y = rainClouds[j]
#         for k in [1,3,5,7]:
#             nx,ny = x+d[k][0],y+d[k][1]
#             if 0<=nx<N and 0<=ny<N and L[ny][nx] > 0:
#                 new_L[y][x] += 1
#     print("new_L: ")         
#     for l in new_L:
#         print(l)
#     new_RainClouds = []
#     for j in range(N):
#         for k in range(N):
#             if [k,j] not in rainClouds:
#                 if new_L[j][k] >= 2:
#                     new_L[j][k] -= 2
#                     new_RainClouds.append([k,j])
#     print("new_L: ")         
#     for l in new_L:
#         print(l)
#     rainClouds = new_RainClouds
#     L = new_L
# print(sum(sum(i) for i in L))

N,M = map(int,input().split())
L = [[*map(int,input().split())] for _ in range(N)]
M = [[*map(int,input().split())] for _ in range(M)]
d = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]] # x y
rainClouds = [[0,N-1],[1,N-1],[0,N-2],[1,N-2]] # x y
v = [[0]*N for _ in range(N)]
for di, si in M:
    for j in range(len(rainClouds)):
        rainClouds[j][0] = (rainClouds[j][0]+d[di-1][0]*si)%N
        rainClouds[j][1] = (rainClouds[j][1]+d[di-1][1]*si)%N
        L[rainClouds[j][1]][rainClouds[j][0]] += 1
        v[rainClouds[j][1]][rainClouds[j][0]] = 1
    new_L = L.copy()
    for x, y in rainClouds:
        for k in [1,3,5,7]:
            nx,ny = x+d[k][0],y+d[k][1]
            if 0<=nx<N and 0<=ny<N and L[ny][nx] > 0:
                new_L[y][x] += 1
    new_RainClouds = []
    for j in range(N):
        for k in range(N):
            if not v[j][k] and new_L[j][k] >= 2:
                new_L[j][k] -= 2
                new_RainClouds.append([k,j])
    rainClouds = new_RainClouds
    L = new_L
    for j in range(N):
        for k in range(N):
            v[j][k] = 0  # 구름 위치 추적 배열 초기화
print(sum(sum(i) for i in L))