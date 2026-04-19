from collections import deque

def solution(priorities, location):
    l = []
    for i,arg in enumerate(priorities):
        l.append((i,arg))
    dq = deque(l)
    answer = 1
    while dq:
        num,level = dq.popleft()
        if not dq: return answer
        if level >= max(x[1] for x in dq):
            if num == location: break
            else: answer += 1
        else: dq.append((num,level))
    return answer

from collections import deque

# def solution(priorities, location):
#     dq = deque((i, p) for i, p in enumerate(priorities))
#     answer = 0

#     while dq:
#         num, level = dq.popleft()

#         if any(level < x[1] for x in dq):
#             dq.append((num, level))
#         else:
#             answer += 1
#             if num == location:
#                 return answer

print(solution([2, 1, 3, 2], 2))