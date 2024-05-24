n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

def check_bishop(board, x, y):
    for i in range(-n,n):
        nx,nxb,ny = (x+i),(x-i),(y+i)
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 2: return False
        if 0 <= nxb < n and 0 <= ny < n and board[nxb][ny] == 2: return False
    return True

def backtrack(possible_positions, board, idx, count):
    if idx == len(possible_positions): return count
    
    x, y = possible_positions[idx]
    max_count = count
    
    if check_bishop(board, x, y):
        board[x][y] = 2
        max_count = max(max_count, backtrack(possible_positions, board, idx + 1, count + 1))
        board[x][y] = 1
    
    max_count = max(max_count, backtrack(possible_positions, board, idx + 1, count))
    return max_count

pos_1 = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1 and (i+j)%2]
pos_2 = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1 and not (i+j)%2]

max_1 = backtrack(pos_1, board, 0, 0)
max_2 = backtrack(pos_2, board, 0, 0)

total_max = max_1 + max_2
print(total_max)