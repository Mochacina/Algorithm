def solution(a, b, n):
    answer = 0
    while n>=a:
        bottle = (n//a)*b # 이번에 받을 병 수
        n = n%a + bottle
        answer += bottle
        print(n)
    return answer

a = 3
b = 1
n = 20
print(solution(a,b,n))