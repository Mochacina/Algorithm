import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

sum = defaultdict(int)
for i in range(n):
    s_a = 0
    for j in range(i,n):
        s_a += A[j]
        sum[s_a] += 1

ans = 0
for i in range(m):
    s_b = 0
    for j in range(i,m):
        s_b += B[j]
        r = T - s_b
        if r in sum:
            ans += sum[r]

print(ans)


# import sys
# from collections import defaultdict

# try:
#     # sys.stdin.readline()을 사용하여 입력을 빠르게 받습니다.
#     T = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     A = list(map(int, sys.stdin.readline().split()))
#     m = int(sys.stdin.readline())
#     B = list(map(int, sys.stdin.readline().split()))
# except (IOError, ValueError) as e:
#     print(f"입력 처리 중 오류 발생: {e}");exit()

# # --- 1. 배열 A의 모든 부 배열의 합 구하기 ---
# # 문제 설명:
# # 먼저, 한쪽 배열(A)의 모든 가능한 부 배열의 합을 계산합니다.
# # 이 합들을 딕셔너리에 저장하여, 특정 합이 몇 번 나타나는지 빈도를 기록합니다.
# # 예를 들어 A = {1, 3, 1} 이면, 부 배열 합은 1, 4, 5, 3, 4, 1이 되고,
# # 딕셔너리는 {1: 2, 3: 1, 4: 2, 5: 1} 와 같이 됩니다.
# # 이 과정의 시간 복잡도는 O(n^2)입니다.

# print("배열 A의 부 배열 합을 계산합니다.")
# sum_a = defaultdict(int)
# for i in range(n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum += A[j]
#         sum_a[current_sum] += 1
# print(f"배열 A의 부 배열 합 계산 완료. 딕셔너리 크기: {len(sum_a)}")

# # --- 2. 배열 B의 부 배열 합을 이용해 정답 찾기 ---
# # 문제 설명:
# # 다음으로, 다른 쪽 배열(B)의 모든 부 배열의 합을 계산합니다.
# # B의 각 부 배열의 합 's_b'가 나올 때마다, 우리가 찾아야 하는 A의 부 배열 합은 'T - s_b'가 됩니다.
# # 미리 계산해 둔 A의 합 딕셔너리에서 'T - s_b'가 몇 번 등장하는지 찾아 그 횟수를 정답에 더합니다.
# # 이 과정의 시간 복잡도는 O(m^2)입니다.
# # 따라서 총 시간 복잡도는 O(n^2 + m^2)이 됩니다.

# print("배열 B의 부 배열 합을 계산하며 정답을 찾습니다.")
# answer = 0
# for i in range(m):
#     current_sum = 0
#     for j in range(i, m):
#         current_sum += B[j]
#         required_sum = T - current_sum
#         if required_sum in sum_a:
#             answer += sum_a[required_sum]
# print("정답 계산 완료.")

# # --- 3. 결과 출력 ---
# print(answer)