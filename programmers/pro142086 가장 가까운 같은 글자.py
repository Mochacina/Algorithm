def solution(s):
    answer = []
    l = [-1]*26
    for n,i in enumerate(s):
        word = ord(i)-97
        if l[word] == -1:
            answer.append(-1)
        else: answer.append(n-l[word])
        l[word] = n
    return answer

s = "foobar"
print("result: ",solution(s))