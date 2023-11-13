def solution(s):
    l = list(map(int, s.split(" ")))
    answer = str(min(l)) + " " + str(max(l))
    return answer

s = "-1 -2 -3 -4"	
print(solution(s))