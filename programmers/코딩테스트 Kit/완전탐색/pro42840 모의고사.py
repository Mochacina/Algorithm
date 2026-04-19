def solution(answers):
    l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    l2 = [2, 1, 2, 3, 2, 4, 2, 5]
    l3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    l=[0]*3
    for i,arg in enumerate(answers):
        if arg == l1[i%len(l1)]: l[0] += 1
        if arg == l2[i%len(l2)]: l[1] += 1
        if arg == l3[i%len(l3)]: l[2] += 1
    if max(l) == l[0]: answer.append(1)
    if max(l) == l[1]: answer.append(2)
    if max(l) == l[2]: answer.append(3)
    return answer

print(solution([1,3,2,4,2]))