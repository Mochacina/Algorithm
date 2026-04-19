# def solution(s):
#     while s:
#         s = s.replace('()','')
#         if s and (s[0] == ")" or s[-1] == "("): return False
#     return True

def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) >= 2 and stack[-2:] == ['(',')']: del stack[-2:]
    return False if stack else True

s = "(())()"	
print(solution(s))