from collections import deque

n, m = map(int, input().split())
l = [input().split() for _ in range(n)]

pos = [(0,1),(1,0),(0,-1),(-1,0)]
v = [[-1]*m for _ in range(n)]
q = deque([])

for y in range(n):
    for x in range(m):
        if l[y][x] == '2':
            q.append((x, y))
            v[y][x] = 0

# BFS
while q:
    x, y = q.popleft()
    for dx, dy in pos:
        xx, yy = x+dx, y+dy
        if 0 <= xx < m and 0 <= yy < n:
            if v[yy][xx] == -1 and l[yy][xx] == '1':
                v[yy][xx] = v[y][x] + 1
                q.append((xx, yy))

out_lines = []
for y in range(n):
    row_out = []
    for x in range(m):
        if l[y][x] == '0':
            row_out.append('0')
        else:
            row_out.append(str(v[y][x]))
    out_lines.append(' '.join(row_out))

print('\n'.join(out_lines))