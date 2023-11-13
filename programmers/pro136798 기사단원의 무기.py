def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        n = 0
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                n+=1
                if j**2 != i: n+=1
                if n > limit: n = power;break
        answer += n
    return answer

number = 10
limit = 3
power = 2

print("answer: ",solution(number, limit, power))