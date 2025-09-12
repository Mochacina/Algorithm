import sys

# 입력 처리를 빠르게 하기 위한 설정! 기본 중의 기본이지.
input = sys.stdin.readline

# 목표 고객 수 C, 도시의 개수 N
c, n = map(int, input().split())

# 각 도시의 홍보 정보 (비용, 고객 수)를 저장할 리스트
promos = []
for _ in range(n):
    cost, customer = map(int, input().split())
    promos.append((cost, customer))

# dp 테이블을 만들 거야. dp[i]는 '정확히 i명의 고객을 모으는 데 드는 최소 비용'을 의미해.
# 목표 고객 C명 이상을 고려해야 하니까, C에 최대 고객 증가 수(100)를 더한 크기로 넉넉하게 만들자.
# 왜냐하면 C명보다 조금 더 많은 고객을 유치하는 게 오히려 더 쌀 수도 있거든!
# 예를 들어, 99명을 모으는 비용이 100원인데, 100명을 모으는 비용이 10원일 수도 있잖아?
dp = [float('inf')] * (c + 101)
dp[0] = 0  # 0명을 모으는 데는 0원이 들지! 당연하잖아?

# 자, 이제 DP 테이블을 채워볼까?
# 각 홍보 방안을 하나씩 순회하면서
for cost, customer in promos:
    # 해당 홍보로 늘어나는 고객 수부터 시작해서 dp 테이블을 업데이트!
    for i in range(customer, c + 101):
        # i명의 고객을 모으는 기존의 최소 비용(dp[i])과
        # (i - customer)명의 고객을 모으는 비용에 현재 홍보 비용(cost)을 더한 값을 비교해서
        # 더 작은 값으로 업데이트하는 거야!
        # dp[i - customer] + cost는 "일단 (i-customer)명 모으고, 이번 홍보를 추가해서 i명을 만들자!"라는 뜻이지.
        if dp[i - customer] != float('inf'): # (i-customer)명을 모으는 방법이 존재할 때만 갱신
            dp[i] = min(dp[i], dp[i - customer] + cost)
    print(dp)
    
# for cost, customer in promos:
#     for i in range(c, c+101):
#         if dp[i-customer] != float('inf'):
#             dp[i] = min(dp[i], dp[i-customer] + cost)
    

# dp 테이블은 C명 이상일 때의 최소 비용들을 모두 계산해뒀어.
# 우리가 원하는 건 '적어도' C명 이상을 모으는 최소 비용이니까,
# dp[c]부터 끝까지의 값들 중에서 가장 작은 값을 찾으면 그게 바로 정답!
result = min(dp[c:])

print(result)

