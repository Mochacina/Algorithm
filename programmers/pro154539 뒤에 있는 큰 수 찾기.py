# def solution(numbers):
#     answer = [0]*len(numbers)
#     mx = 0
#     for n, i in enumerate(numbers[::-1]):
#         mx = max(mx,i)
#         answer[n] = -1 if mx==i else mx
        
#     return answer[::-1]

def solution(numbers):
    stack = []  # 스택을 이용하여 뒷 큰수를 찾습니다.
    result = [-1] * len(numbers)  # 결과 배열을 -1로 초기화합니다.

    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            result[idx] = numbers[i]
        
        stack.append(i)
    
    return result

numbers = [9, 1, 5, 3, 6, 2]		
print(solution(numbers))    