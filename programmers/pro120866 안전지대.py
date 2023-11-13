def solution(board):
    dis = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    board_len = len(board)
    mine = 0
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == 1:
                mine += 1
                for node in dis:
                    x,y = node
                    if i+x >= 0 and j+y >= 0 and i+x < board_len and j+y < board_len:
                        if board[i+x][j+y] == 0:
                            board[i+x][j+y] = 2
                            mine += 1
    return board_len**2-mine
                

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	
print(solution(board))