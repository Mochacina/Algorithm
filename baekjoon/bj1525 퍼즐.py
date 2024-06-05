from collections import deque

di = [(0,1),(1,0),(0,-1),(-1,0)]

def s(board): #serialize
    return ''.join(''.join(row) for row in board)

def d(state): #deserialize
    return [list(state[i:i+3]) for i in range(0, 9, 3)]

l = [[*input().split()] for _ in range(3)]
l = s(l)

q = deque([(l, 0)])
visited = set([l])
def bfs():
    while q:
        state, cnt = q.popleft()
        if s(state) == '123456780':
            return cnt
        board = d(state)
        x, y = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '0'][0]
        
        for dx, dy in di:
            nx, ny = x+dx, y+dy
            if 0 <= nx <= 2 and 0 <= ny <= 2:
                n_board = [r[:] for r in board]
                n_board[nx][ny], n_board[x][y] = n_board[x][y], n_board[nx][ny]
                n_board = s(n_board)
                if s(n_board) not in visited:
                    visited.add(n_board)
                    q.append((s(n_board),cnt+1))
        
    return -1

print(bfs())