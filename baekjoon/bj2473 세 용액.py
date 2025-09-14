# import sys

# n = int(sys.stdin.readline())
# solutions = list(map(int, sys.stdin.readline().split()))

# # 1. 용액 리스트를 오름차순으로 정렬합니다.
# solutions.sort()

# # 0에 가장 가까운 합을 저장할 변수, 초기값은 매우 큰 수로 설정합니다.
# min_sum = float('inf')

# # 최종 결과를 저장할 리스트입니다.
# final_answer = []

# # 2. 하나의 용액(i)을 고정하고, 나머지에 대해 투 포인터 탐색을 수행합니다.
# for i in range(n - 2):
#     # 고정된 용액
#     fixed_solution = solutions[i]
    
#     # 3. 투 포인터 설정
#     left = i + 1
#     right = n - 1

#     while left < right:
#         # 세 용액의 합 계산
#         current_sum = fixed_solution + solutions[left] + solutions[right]

#         # 4. 합의 절댓값이 기존 최솟값보다 작으면 정답을 갱신합니다.
#         if abs(current_sum) < min_sum:
#             min_sum = abs(current_sum)
#             final_answer = [fixed_solution, solutions[left], solutions[right]]

#         # 5. 포인터 이동
#         # 합이 0보다 작으면 합을 키우기 위해 left 포인터를 이동합니다.
#         if current_sum < 0:
#             left += 1
#         # 합이 0보다 크면 합을 줄이기 위해 right 포인터를 이동합니다.
#         elif current_sum > 0:
#             right -= 1
#         # 합이 0이면 완벽한 답이므로 즉시 종료합니다.
#         else:
#             exit(print(*final_answer))

# # 최종적으로 찾은 세 용액을 출력합니다.
# # final_answer에 담긴 값들은 이미 오름차순이 보장됩니다.
# print(*final_answer)

import sys

input = sys.stdin.readline
n = int(input())
solutions = sorted(list(map(int,input().split())))
min_sum = float('inf')
final_answer = []

for i in range(n-2):
    solution = solutions[i]
    l = i+1
    r = n-1
    
    while l < r:
        current_sum = solution + solutions[l] + solutions[r]
        
        if abs(current_sum) < min_sum:
            min_sum = abs(current_sum)
            ans = [solution, solutions[l], solutions[r]]
        
        if current_sum < 0: l += 1
        elif current_sum > 0: r -= 1
        else: exit(print(*ans))
        
print(*ans)