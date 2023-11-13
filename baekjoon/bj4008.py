def calculate_adjusted_power(n, coefficients, powers):
    a, b, c = coefficients
    
    # 특공대의 전투력 계산 함수
    def calculate_power(x):
        return a * x**2 + b * x + c
    
    # 전체 병사들을 특공대로 나누고 조정된 전투력의 합 계산
    total_adjusted_power = sum(calculate_power(power) for power in powers)
    
    return total_adjusted_power


# 입력 받기
n = int(input())
coefficients = list(map(int, input().split()))
powers = list(map(int, input().split()))

# 최대 조정된 전체 전투력 계산
max_adjusted_power = calculate_adjusted_power(n, coefficients, powers)

# 결과 출력
print(max_adjusted_power)