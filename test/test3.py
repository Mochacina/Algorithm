n = int(input())
board = [[*map(int,input().split())]for _ in range(n)]
x,y = 0,0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            x=i
            y=j
print(x, y)

for i in range(-n,n):
    nx = (x+i)
    ny = (y+i)
    nxb = (x-i)
    if 0 <= nx < n and 0 <= ny < n :
        board[nx][ny] = 1
    if 0 <= nxb < n and 0 <= ny < n :
        board[nxb][ny] = 1
    


for i in board:
    print(*i)

print(0xffffffff | 0xffffff00)