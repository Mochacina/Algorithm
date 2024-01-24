def BFS(x,y,l):
    visited = [[0]*c for _ in range(r)]
    queue=[(x,y,0)]
    visited[y][x] = 1 
    while queue:
        rx,ry,num = queue.pop(0)
        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            px,py = dir
            nx,ny = rx+px,ry+py
            if l[ny][nx] == 'G':
                return f"Shortest Path: {num+1}"
            if not visited[ny][nx] and l[ny][nx] in ['O','0']:
                visited[ny][nx] = 1
                queue.append((nx,ny,num+1))
    return "No Exit"

for _ in range(int(input())):
    r,c = map(int, input().split())
    l = [input() for _ in range(r)]
    for y in range(0,r):
        for x in range(0,c):
            if l[y][x]=='S':
                print(BFS(x,y,l))