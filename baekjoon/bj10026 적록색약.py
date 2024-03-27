def bfs(x, y, blindness):
    visited = visited1 if not blindness else visited2
    visited[y][x] = 1
    if blindness:
        colors = ['B'] if l[y][x] == 'B' else ['G','R']
    else: colors = [l[y][x]]
    node = [(x,y)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while node:
        _x, _y = node.pop()
        for nx, ny in direction:
            _x2, _y2 = _x+nx, _y+ny
            if 0 <= _x2 < n and 0 <= _y2 < n and not visited[_y2][_x2] and l[_y2][_x2] in colors:
                visited[_y2][_x2] = 1
                node.append((_x2,_y2))

n = int(input())
visited1 = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
l = [input() for _ in range(n)]
a,b = 0,0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(j, i, False)
            a+=1
        if not visited2[i][j]:
            bfs(j, i, True)
            b+=1
print(a,b)