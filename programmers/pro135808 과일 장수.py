def solution(k, m, score):
    answer = 0
    l = sorted(score)
    while len(l)>=m:
        l2 =[]
        for _ in range(m):
            l2.append(l.pop())
        answer += min(l2)*len(l2)
    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
print(solution(k,m,score))