# def solution(n):
#     answer = 0
#     l = [0]*(n+1)
#     for i in range(1,n+1):
#         l[i] = l[i-1]+i
#     for i in range(1,n+1):
#         for j in range(i):
#             if l[i]-l[j] == n:
#                 answer += 1
#                 break
#     return answer

def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum > n: break
            elif sum == n:
                answer += 1
                break
    return answer

n = 15
print(solution(n))