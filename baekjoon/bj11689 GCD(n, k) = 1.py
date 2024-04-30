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
#     result = n   # ������ �� ����� n���� �ʱ�ȭ
#     p = 2        # ���� ���� �Ҽ����� ����

#     # n�� ���μ������ϸ鼭 �� ���μ��� ���� ���
#     while p * p <= n:
#         if n % p == 0:  # p�� n�� ���μ��� ���
#             while n % p == 0:
#                 n //= p
#             result -= result // p  # ���Ϸ� �� �Լ��� ��� �κ�
#         p += 1

#     # ���� n�� 1���� ũ�� n ��ü�� �Ҽ�
#     if n > 1:
#         result -= result // n

#     return result

# # �Լ� ��� ����
# n = int(input("�ڿ��� n�� �Է��ϼ���: "))
# print(f"{n}�� ���μ��� ������ ������ {euler_phi(n)}�� �Դϴ�.")
