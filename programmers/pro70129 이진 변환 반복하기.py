def solution(s):
    answer = [0,0]
    while s != "1":
        n = len([i for i in s if i == "1"])
        answer[0] += 1
        answer[1] += (len(s)-n)
        s = format(n, 'b')
    return answer

s = "110010101001"

print(solution(s))