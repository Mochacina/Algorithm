import math

# 입력 받기
X1, Y1, Z1,X2, Y2, Z2 = map(int, input().split())
N = int(input())
K = [*map(int,input().split())]

# 시작점과 끝점 사이의 거리 계산
D = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 + (Z2 - Z1)**2)

# 막대기 길이의 합 계산
total_length = sum(K)
max_length = max(K)

# 결과 확인 및 출력
if total_length - D > -1e-9: 
    if max_length - (total_length-max_length) <= D: exit(print("YES"))
print("NO")