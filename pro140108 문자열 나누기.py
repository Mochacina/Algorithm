def solution(s):
    answer = []
    l = []
    fw = 0
    for i in s:
        if len(l) == 0: # 초기화됐을떄
            fw = i
        l.append(i)
        n = l.count(fw)
        if len(l)-n == n:
            answer.append(l)
            l = []
    if len(l): answer.append(l)
    print(answer)
    return len(answer)


s = "banana"			
print(solution(s))