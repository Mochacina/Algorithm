def solution(n):
    if n in [1,2] : return 0
    answer = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                answer += 1
                break
    return answer

k = 100

print(solution(k))