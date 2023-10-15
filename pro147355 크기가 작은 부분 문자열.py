def solution(t, p):
    answer = 0
    for n in range(len(t)-(len(p)-1)):
        print(t[n:n+len(p)])
        if int(t[n:n+len(p)]) <= int(p): answer += 1
    return answer

t = "500220839878"		
p = "7"		
print(f"result: {solution(t,p)}")