N, M = map(int, input().split())
house = []
kfc = []
for i in range(N):
    l = [*map(int, input().split())]
    for j in range(N):
        if l[j] == 1:
            house.append([j, i])
        elif l[j] == 2:
            kfc.append([j, i])
distance = [[0]*len(kfc) for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(kfc)):
        distance[i][j] = abs(house[i][0]-kfc[j][0])+abs(house[i][1]-kfc[j][1])
        
v=[0]*len(kfc)
chicken_distance = 999999999
def dfs(a,s=[]):
    global chicken_distance
    if len(s) == M:
        chicken_distance = min(chicken_distance, sum([min([distance[i][j] for j in s])for i in range(len(house))]))
        return
    for i in range(a,len(kfc)):
        if not v[i]:
            v[i]=1
            dfs(i+1,s+[i])
            v[i]=0
dfs(0)
print(chicken_distance)