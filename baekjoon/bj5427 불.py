import sys
from collections import deque

input = sys.stdin.readline
dir = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(q):
    while q:
        type, x, y, cnt = q.popleft()
        if type == '@':
            cnt+=1
            if x in [0,h-1] or y in [0,w-1]:
                return cnt
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if 0 <= nx < h and 0 <= ny < w and l[nx][ny] not in ['#','*',type]:
                l[nx][ny] = type
                q.append((type,nx,ny,cnt))
    return "IMPOSSIBLE"

for _ in ' '*int(input()):
    w,h = map(int,input().split())
    l = [[*input()][:-1]for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if l[i][j] == '*': q.appendleft(('*',i,j,0))
            elif l[i][j] == '@': q.append(('@',i,j,0))
    print(bfs(q))