import math

# �Է� �ޱ�
X1, Y1, Z1,X2, Y2, Z2 = map(int, input().split())
N = int(input())
K = [*map(int,input().split())]

# �������� ���� ������ �Ÿ� ���
D = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 + (Z2 - Z1)**2)

# ����� ������ �� ���
total_length = sum(K)
max_length = max(K)

# ��� Ȯ�� �� ���
if total_length - D > -1e-9: 
    if max_length - (total_length-max_length) <= D: exit(print("YES"))
print("NO")