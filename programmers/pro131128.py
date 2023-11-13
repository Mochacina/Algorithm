# def solution(X, Y):
#     answer = ''
#     y = [i for i in Y]
#     for i in X:
#         if i in y:
#             y.remove(i)
#             answer += i
#     return f"{int(''.join(sorted(answer)[::-1]))}" if len(answer) else "-1"

def solution(X, Y):
    l = [min(X.count(str(i)),Y.count(str(i))) for i in range(10)]
    answer = ''.join([f"{9-n}"*i for n, i in enumerate(l[::-1]) if i > 0]) if sum(l[1:])>0 else "0"
    return answer if sum(l)!=0 else "-1"

X = "100"		
Y = "2345"		

print(solution(X,Y))
