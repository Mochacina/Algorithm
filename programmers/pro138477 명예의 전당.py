def solution(k, score):
    l = []
    answer = []
    for i in score:
        l.append(i)
        if len(l) > k:del l[l.index(min(l))]
        answer.append(min(l))
    return answer

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	
print(solution(k,score))