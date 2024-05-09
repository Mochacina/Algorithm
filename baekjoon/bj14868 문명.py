# bfs 진행하면서 빈 공간일경우 문명 전파
# 다른 문명일 경우 문명을 하나로 묶음
# 모든 문명이 하나로 묶이면 종료

from collections import deque

n,k = map(int, input().split())
l = [[0]*n for _ in range(n)]
civ_node = deque([])
civ_cnt = k
times = 0
parent = [i for i in range(k+1)]
di = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(k):
    x, y = map(int, input().split())
    l[x-1][y-1] = i+1
    civ_node.append((x-1,y-1))
    
def bfs(q):
    q_next = deque([])
    while q:
        x,y = q.popleft()
        civ = l[x][y]
        for dx,dy in di:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if not l[nx][ny]:
                    l[nx][ny] = civ
                    q_next.append((nx,ny))
    return q_next

def civ_combine(q):
    for node in q:
        x,y = node
        civ = l[x][y]
        for dx,dy in di:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if l[nx][ny] and l[nx][ny] != civ:
                    u(civ, l[nx][ny])

def f(a):
    if a!=parent[a]:
        parent[a] = f(parent[a])
    return parent[a]

def u(a,b):
    global civ_cnt
    rootA = f(a)
    rootB = f(b)
    if rootA != rootB:
        if rootB > rootA:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
        civ_cnt -= 1

while 1:
    civ_combine(civ_node)
    if civ_cnt == 1: break
    civ_node = bfs(civ_node)
    times += 1

print(times)