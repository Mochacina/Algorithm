# import sys

# # Hmph! For this genius beautiful girl programmer, Lady Helena, it's absolutely a piece of cake!

# def solve():
#     """
#     This function solves the Baekjoon problem 15824.
#     Yes! I am the one and only Helena!
#     """
#     # --- 입력 처리 ---
#     # 어서 와, N이랑 스코빌 지수들을 이리 내놔!
#     try:
#         n_str = sys.stdin.readline()
#         if not n_str: return
#         n = int(n_str)
#         scovilles = list(map(int, sys.stdin.readline().split()))
#     except (IOError, ValueError) as e:
#         # 흥, 입력이 이상하잖아! 이 헬레나 님을 귀찮게 하다니.
#         print(f"Debug: Invalid input, terminating. Error: {e}", file=sys.stderr)
#         return

#     # --- 핵심 로직 ---
#     # 먼저 정렬부터 하는 게 기본 소양이지!
#     scovilles.sort()
#     print(f"Debug: Sorted scovilles: {scovilles}", file=sys.stderr)

#     MOD = 1_000_000_007

#     # 2의 거듭제곱을 미리 계산해두는 센스!
#     # powers[i]는 2^i % MOD 야.
#     powers = [1] * n
#     for i in range(1, n):
#         powers[i] = (powers[i-1] * 2) % MOD
    
#     print(f"Debug: Precomputed powers of 2 (mod {MOD}) up to {n-1}", file=sys.stderr)

#     total_pain = 0
    
#     # 자, 이제 각 원소가 기여하는 고통을 모두 더해주겠어!
#     for i in range(n):
#         # scovilles[i]가 최댓값이 되는 경우의 수: 2^i
#         # scovilles[i]가 최솟값이 되는 경우의 수: 2^(n-1-i)
        
#         # scovilles[i] * (2^i - 2^(n-1-i))
#         term = (powers[i] - powers[n - 1 - i] + MOD) % MOD
#         pain_contribution = (scovilles[i] * term) % MOD
        
#         total_pain = (total_pain + pain_contribution) % MOD
        
#         print(f"Debug: i={i}, score={scovilles[i]}, term=({powers[i]} - {powers[n-1-i]}) -> {term}, contribution={pain_contribution}, total_pain={total_pain}", file=sys.stderr)

#     # --- 출력 ---
#     # 어때, 완벽하지? 이 몸의 실력에 감탄하라구!
#     print(total_pain)

# if __name__ == "__main__":
#     solve()


import sys

input = sys.stdin.readline
n = int(input())
scovilles = sorted(list(map(int, sys.stdin.readline().split())))

MOD = 1000000007

power = [1]*n
for i in range(1,n): power[i] = (power[i-1] * 2) % MOD
total_pain = 0

for i in range(n):
    term = (power[i] - power[n - 1 - i] + MOD) % MOD
    pain_contribution = (scovilles[i] * term) % MOD
    total_pain = (total_pain + pain_contribution) % MOD

print(total_pain)