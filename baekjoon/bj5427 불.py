import sys
from collections import deque

input = sys.stdin.readline

def bfs(q):
    cnt = 0
    while q:
        type, x, y = q.popleft()
        print(type,x,y)
        if type == '@':
            cnt+=1
            if x in [0,h] or y in [0,w]:
                return cnt
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0 <= nx < x and 0 <= ny < y:
                if l[nx][ny] == '.':
                    l[nx][ny] = type
                    q.append((type,nx,ny))
        print(l)
    return "IMPOSSIBLE"

for _ in ' '*int(input()):
    w,h = map(int,input().split())
    l = [[*input()]for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if l[i][j] == '*': q.appendleft(('*',i,j))
            elif l[i][j] == '@': q.append(('@',i,j))
    print(q)
    print(bfs(q))