def solution(targets):
    answer=0
    targets.sort(key=lambda x:(x[1],x[0]))
    s,e = 0,0
    
    for node in targets:
        n,m = node
        if n >= e:
            e = m
            answer += 1
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	
print(solution(targets))