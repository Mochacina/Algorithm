def solution(A,B):
    answer = []
    
    A = sorted(A)
    B = sorted(B)[::-1]
    
    for i in range(len(A)): answer.append(A[i]*B[i])

    return sum(answer)

A = [1, 2]
B = [3, 4]

print(solution(A,B))