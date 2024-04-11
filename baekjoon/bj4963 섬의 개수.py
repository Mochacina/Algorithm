while 1:
    w,h = map(int, input().split())
    if not (w or h): break
    l = [list(map(int, input().split())) for _ in range(h)]
    v = [[0]*w for _ in range(h)]
    n = 0
    for i in range(h):
        for j in range(w):
            if l[i][j] == 1 and not v[i][j]:
                v[i][j] = 1;n += 1
                q = [(i,j)]
                while q:
                    x,y = q.pop()
                    # 8 directions
                    for dx, dy in [[x,y] for x in [-1,0,1] for y in [-1,0,1] if x or y]:
                        nx, ny = x+dx, y+dy
                        if nx<0 or ny<0 or nx>=h or ny>=w: continue
                        if not v[nx][ny] and l[nx][ny]:
                            v[nx][ny] = 1
                            q.append((nx,ny))
    print(n)