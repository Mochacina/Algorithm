m,n = map(int,input().split())
l = [[*map(int,input().split())]for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

di = [(0,1),(1,0),(0,-1),(-1,0)]

def dfs(x,y):
    if x==m-1 and y==n-1: return 1
    