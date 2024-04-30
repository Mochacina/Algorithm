def euler_phi(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result

n = int(input())
print(euler_phi(n))

# def euler_phi(n):
#     result = n   # 시작할 때 결과를 n으로 초기화
#     p = 2        # 가장 작은 소수부터 시작

#     # n을 소인수분해하면서 각 소인수에 대해 계산
#     while p * p <= n:
#         if n % p == 0:  # p가 n의 소인수인 경우
#             while n % p == 0:
#                 n //= p
#             result -= result // p  # 오일러 피 함수의 계산 부분
#         p += 1

#     # 남은 n이 1보다 크면 n 자체가 소수
#     if n > 1:
#         result -= result // n

#     return result

# # 함수 사용 예시
# n = int(input("자연수 n을 입력하세요: "))
# print(f"{n}과 서로소인 숫자의 개수는 {euler_phi(n)}개 입니다.")
