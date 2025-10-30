MOD = 1000000007

def mod_inv(a, mod=MOD):
    return pow(a, mod - 2, mod)

M = int(input())
result = 0

for _ in range(M):
    N, S = map(int, input().split())
    expectation = (S * mod_inv(N)) % MOD
    result = (result + expectation) % MOD

print(result)