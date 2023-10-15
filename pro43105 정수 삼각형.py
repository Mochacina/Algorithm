def solution(triangle):
    n = len(triangle[-1])
    mem = [[-1] * n for _ in range(n)]
    for i in range(n): # 층 수
        for j in range(i+1): # 너비
            if i == 0: mem[i][i] = triangle[i][i]
            else: 
                if j == 0: mem[i][j] = mem[i-1][j]+triangle[i][j]
                elif j == i: mem[i][j] = mem[i-1][j-1]+triangle[i][j]
                else: mem[i][j] = max(mem[i-1][j]+triangle[i][j], mem[i-1][j-1]+triangle[i][j])
    return max(mem[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


print(f"result: {solution(triangle)}")


# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5