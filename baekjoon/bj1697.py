from collections import deque

def bfs(n,k):
    d = deque()
    d.append(n)
    while d:
        i = d.popleft()
        if i == k: print(l[k]);exit()
        for j in [i+1, i-1, i*2]:
            if 0 <= j <= max and l[j]==0:
                l[j] = l[i]+1
                d.append(j)
max = 100001
n,k = map(int, input().split())
l = [0]*(max+1)
bfs(n,k)