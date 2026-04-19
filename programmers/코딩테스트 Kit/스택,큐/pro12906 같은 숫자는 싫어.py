def solution(arr):
    answer = []
    n = -1
    
    for i in arr:
        if n != i:
            n = i
            answer.append(n)
    
    return answer

arr = [4,4,4,3,3]

print(solution(arr))