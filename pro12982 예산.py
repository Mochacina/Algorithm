def solution(d, budget):
    sum = 0
    answer = 0
    for i in sorted(d):
        if sum+i > budget: break
        sum += i
        answer += 1
    return answer

d = [2,2,3,3]	
budget = 10

print(solution(d, budget))