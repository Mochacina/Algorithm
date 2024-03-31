N = int(input())
l = [[0 for _ in range(N)] for _ in range(N)]
stu = [list(map(int, input().split())) for _ in range(N*N)]
for s in stu:
    num = s[0]
    like = s[1:]
    position_list = []
    for i in range(N):
        for j in range(N):
            if l[i][j] == 0:
                blank = 0
                friend = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if l[nx][ny] == 0:
                            blank += 1
                        elif l[nx][ny] in like:
                            friend += 1
                position_list.append((i, j, blank, friend))
    position_list.sort(key=lambda x: (-x[3], -x[2], x[0], x[1]))
    l[position_list[0][0]][position_list[0][1]] = num

ans = 0
stu.sort(key=lambda x: x[0])
for i in range(N):
    for j in range(N):
        cnt = 0
        num = l[i][j]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                if l[nx][ny] in stu[num-1][1:]:
                    cnt += 1
        ans += 10 ** cnt // 10
print(ans)
        