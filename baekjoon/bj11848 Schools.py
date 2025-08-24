import heapq
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
a = []

for i in range(n):
    music, sport = map(int, input().split())
    a.append((music, sport))

# 정렬: (음악지망생 - 체육지망생) 내림차순
# C++의 람다와 동일한 정렬 기준
a.sort(key=lambda x: x[0] - x[1], reverse=True)

# L 배열 계산 (음악학교 배치)
L = [-float('inf')] * (n + 1)  # L[0]부터 L[n]까지
q = []  # 최소 힙 (파이썬 heapq는 기본적으로 최소 힙)
sum_val = 0

for i in range(n):
    # C++에서는 1-based, 파이썬에서는 0-based이므로 조정
    music_students = a[i][0]
    heapq.heappush(q, music_students)  # 최소 힙에 직접 저장
    sum_val += music_students
    
    if len(q) < m:
        L[i + 1] = -float('inf')  # 아직 m개가 안됨
    elif len(q) == m:
        L[i + 1] = sum_val  # 정확히 m개
    else:  # m개 초과
        min_val = heapq.heappop(q)  # 가장 작은 값 제거
        sum_val -= min_val
        L[i + 1] = sum_val

# R 배열 계산 (체육학교 배치)
R = [-float('inf')] * (n + 2)  # R[1]부터 R[n+1]까지 (R[n+1] = 0)
q = []  # 큐 초기화
sum_val = 0

for i in range(n - 1, -1, -1):  # 역순으로 처리
    sport_students = a[i][1]
    heapq.heappush(q, sport_students)
    sum_val += sport_students
    
    if len(q) < t:
        R[i + 1] = -float('inf')
    elif len(q) == t:
        R[i + 1] = sum_val
    else:  # t개 초과
        min_val = heapq.heappop(q)
        sum_val -= min_val
        R[i + 1] = sum_val

# R[n+1] = 0 (아무 학교도 선택하지 않는 경우)
R[n + 1] = 0 if t == 0 else -float('inf')

# 최종 답 계산
ans = 0
for i in range(n + 1):  # i는 0부터 n까지
    if L[i] != -float('inf') and R[i + 1] != -float('inf'):
        ans = max(ans, L[i] + R[i + 1])

print(ans)

# import heapq
# import sys
# input = sys.stdin.readline

# n, m, t = map(int, input().split())
# a = []

# for i in range(n):
#     music, sport = map(int, input().split())
#     a.append((music, sport))

# a.sort(key=lambda x: x[0] - x[1], reverse=True)

# L = [-float('inf')] * (n + 1)
# q = []
# sum_val = 0

# for i in range(n):
#     music_students = a[i][0]
#     heapq.heappush(q, music_students)
#     sum_val += music_students
    
#     if len(q) < m:
#         L[i + 1] = -float('inf')
#     elif len(q) == m:
#         L[i + 1] = sum_val
#     else:
#         min_val = heapq.heappop(q)
#         sum_val -= min_val
#         L[i + 1] = sum_val

# R = [-float('inf')] * (n + 2)
# q = []
# sum_val = 0

# for i in range(n - 1, -1, -1):
#     sport_students = a[i][1]
#     heapq.heappush(q, sport_students)
#     sum_val += sport_students
    
#     if len(q) < t:
#         R[i + 1] = -float('inf')
#     elif len(q) == t:
#         R[i + 1] = sum_val
#     else:
#         min_val = heapq.heappop(q)
#         sum_val -= min_val
#         R[i + 1] = sum_val

# R[n + 1] = 0 if t == 0 else -float('inf')

# ans = 0
# for i in range(n + 1):
#     if L[i] != -float('inf') and R[i + 1] != -float('inf'):
#         ans = max(ans, L[i] + R[i + 1])

# print(ans)