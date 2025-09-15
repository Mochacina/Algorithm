n=int(input())
ans=[0]*10
add=0
i=1
while n!=0:
    c=n%10
    n//=10
    ans[0]-=i
    for j in range(c):ans[j] += (n+1)*i
    ans[c] += n*i+1+add
    for j in range(c+1,10):ans[j] += n*i
    add+=c*i
    i*=10
print(" ".join(map(str,ans)))

# import sys
# n = sys.stdin.readline().strip()
# ans = [0]*10

# def solve(n_str):
#     num = int(n_str)
#     length = len(n_str)
#     res = [0] * 10
    
#     for i, digit_char in enumerate(n_str):
#         digit = int(digit_char)
        


# import sys

# n_str = sys.stdin.readline().strip()
# n = int(n_str)
# ans = [0] * 10

# # 0부터 N까지 각 숫자의 개수를 세는 함수
# # 마지막에 1~N 범위에 맞게 0의 개수를 보정
# def count_digits(num_str):
#     num = int(num_str)
#     length = len(num_str)
#     res = [0] * 10
    
#     for i, digit_char in enumerate(num_str):
#         digit = int(digit_char)
#         power_of_10 = 10**(length - 1 - i)
        
#         # 1. 앞자리(prefix)에 대한 기여분 계산
#         # 예: 54321에서 '4'를 분석할 때, 00xxx ~ 53xxx 까지의 범위
#         # 0부터 (prefix-1)까지는 현재 자릿수에 0~9가 모두 power_of_10번씩 나옴
#         prefix = int(num_str[:i]) if i > 0 else 0
#         for d in range(10):
#             res[d] += prefix * power_of_10
        
#         # 2. 현재 자릿수(digit)에 대한 기여분 계산
#         # 2-1. 0부터 (digit-1)까지의 숫자들
#         # 예: 54321에서 '4'를 분석할 때, 50xxx ~ 53xxx 범위
#         # 현재 자릿수(천의 자리)에 0, 1, 2, 3이 각각 power_of_10번씩 나옴
#         for d in range(digit):
#             res[d] += power_of_10
        
#         # 2-2. 현재 자릿수가 digit인 경우
#         # 예: 54321에서 '4'를 분석할 때, 54000 ~ 54321 범위
#         # 뒷자리(suffix) 수만큼 현재 digit이 더 나타남
#         suffix = int(num_str[i+1:]) if i < length - 1 else 0
#         res[digit] += suffix + 1
        
#     # 0의 개수 보정 (leading zeros 제거)
#     # 0, 00~09, 000~099 ... 에 해당하는 0들을 제거
#     # 1, 10, 100, ...
#     zero_correction = 0
#     for i in range(length):
#         zero_correction += 10**i
#     res[0] -= zero_correction
    
#     return res

# ans = count_digits(n_str)
# print(*ans)