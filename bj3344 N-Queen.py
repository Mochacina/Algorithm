# import sys
# sys.setrecursionlimit(10**6)

# def is_safe(board, row, col, n):
#     # 같은 열에 퀸이 있는지 확인
#     for i in range(row):
#         if board[i] == col or abs(board[i] - col) == abs(i - row):
#             return False
#     return True

# def print_solution(board, n):
#     for i in range(n):
#         print(board[i] + 1)

# def solve_n_queens(n):
#     board = [-1] * n  # 각 행에 있는 퀸의 열 위치를 저장

#     def dfs(row):
#         if row == n:
#             print_solution(board, n)
#             return True
#         for col in range(n):
#             if is_safe(board, row, col, n):
#                 board[row] = col
#                 if dfs(row + 1):
#                     return True
#                 board[row] = -1  # 백트래킹
#         return False

#     if not dfs(0):
#         print("No solution")

# # 입력 받기
# N = int(input())
# solve_n_queens(N)

def place_queens(n):
    # 규칙에 따라 퀸을 배치할 위치를 정의하는 리스트
    even_list = list(range(2, n+1, 2))
    odd_list = list(range(1, n+1, 2))
    
    if n % 6 == 2:
        # 나머지가 2인 경우, 1과 3을 교환하고 5를 끝으로 이동
        odd_list = [3, 1] + odd_list[2:]
        odd_list.append(odd_list.pop(odd_list.index(5)))
    elif n % 6 == 3:
        # 나머지가 3인 경우, 짝수 리스트에서 2를 끝으로 이동하고,
        # 홀수 리스트에서 1, 3을 끝으로 이동
        even_list.append(even_list.pop(even_list.index(2)))
        odd_list.append(odd_list.pop(odd_list.index(1)))
        odd_list.append(odd_list.pop(odd_list.index(3)))
    
    # 짝수 리스트와 홀수 리스트를 병합
    position_list = even_list + odd_list
    
    # 퀸의 위치를 출력
    for i in position_list:
        print(i)

# 입력 받기
N = int(input())
place_queens(N)

