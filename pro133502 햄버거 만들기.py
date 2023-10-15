from collections import deque
def solution(ingredient):
    answer = 0
    stack = []
    ingredient = ingredient[::-1]
    while ingredient:
        stack.append(ingredient.pop())
        if len(stack) > 3 and stack[-4:] == [1,2,3,1]:
            answer += 1
            [stack.pop() for _ in range(4)]
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]			
print("result:", solution(ingredient))