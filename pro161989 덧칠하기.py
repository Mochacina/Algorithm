# def solution(n, m, section):
#     l = [0]*n
#     answer = 0
#     for i in section: l[i-1] = 1
#     for n, i in enumerate(l):
#         if i == 1:
#             answer += 1
#             for j in range(n,n+m): 
#                 if j < len(l): l[j] = 0
#     return answer

def solution(n, m, section):
    p = 1
    answer = 0
    while p <= n:
        if p in section: 
            p+=m
            answer += 1
        else: p+=1
    return answer

n = 8
m = 4
section = [2, 3, 6]

print(solution(n,m,section))