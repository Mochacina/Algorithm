def solution(n, computers):
    visited = [0]*n
    stack = []
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = 1
            stack.append(i)
            while stack:
                node = stack.pop()
                for j in range(n):
                    if j!=node and not visited[j] and computers[node][j]:
                        stack.append(j)
                        visited[j] = 1
    
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	
print(solution(n, computers))