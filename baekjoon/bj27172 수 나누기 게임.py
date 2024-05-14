# def calculate_scores(N, cards):
#     from collections import defaultdict
    
#     divisor_map = defaultdict(list)
#     for i in range(N):
#         x = cards[i]
#         for j in range(1, int(x**0.5) + 1):
#             if x % j == 0:
#                 divisor_map[j].append(i)
#                 if j != x // j:
#                     divisor_map[x // j].append(i)
    
#     scores = [0] * N
    
#     for i in range(N):
#         x = cards[i]
#         for d in divisor_map[x]:
#             if d != i:
#                 scores[i] -= 1
#                 scores[d] += 1
    
#     return scores

# N = int(input())
# cards = list(map(int, input().split()))
# scores = calculate_scores(N, cards)
# print(' '.join(map(str, scores)))

# def calculate_scores(nums):
#     n = len(nums)
#     nums = sorted((num, i) for i, num in enumerate(nums))
#     scores = [0] * n

#     # 각 수에 대해 가능한 모든 배수 관계 검토
#     for j in range(n):
#         xj, idx_j = nums[j]
#         for i in range(j + 1, n):
#             xi, idx_i = nums[i]
#             if xi % xj == 0:  # xi가 xj의 배수인 경우
#                 scores[idx_j] += 1
#                 scores[idx_i] -= 1

#     return scores

# N = int(input())
# numbers = list(map(int, input().split()))

# final_scores = calculate_scores(numbers)
# print(' '.join(map(str, final_scores)))

N = int(input())
num = [*map(int, input().split())]
num_s = set(num)
num_m = max(num)
score = [0]*(num_m+1)
l = [[] for _ in range(num[-1]+1)]

for n in num:
    for m in range(n*2, num_m+1, n):
        if m in num_s:
            score[n] += 1
            score[m] -= 1

print(' '.join(map(str,[score[n] for n in num])))