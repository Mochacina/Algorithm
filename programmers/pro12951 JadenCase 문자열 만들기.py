def solution(s):
    answer = ''
    isJaden = 1
    for i in s:
        if isJaden:
            answer+=i.upper()
            isJaden = 0
        else: answer+=i.lower()
        if i == " ": isJaden = 1
    return answer

s = "for the last week"
print(solution(s))