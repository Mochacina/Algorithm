mod = 10007

MAXN = 52
C = [[0]*(MAXN+1) for _ in range(MAXN+1)]
for i in range(MAXN+1):
    C[i][0] = 1
    for j in range(1,i+1):
        C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod

import sys
N = int(sys.stdin.readline().strip())

ans = 0
maxk = min(13,N//4)
for k in range(1,maxk+1):
    r = 52 - 4*k
    n = N - 4*k
    n1 = C[13][k]
    n2 = C[r][n] if 0 <= n <= r else 0
    term = (n1 * n2) % mod

    ans = ((ans + term) if (k%2)==1 else (ans - term)) % mod

print(ans % mod)

# MOD = 10007

# MAXN = 52
# C = [[0]*(MAXN+1) for _ in range(MAXN+1)]
# for n in range(MAXN+1):
#     C[n][0] = 1
#     for r in range(1, n+1):
#         C[n][r] = (C[n-1][r-1] + C[n-1][r]) % MOD

# import sys
# N = int(sys.stdin.readline().strip())

# ans = 0
# maxk = min(13, N//4)
# for k in range(1, maxk+1):
#     rem = 52 - 4*k
#     need = N - 4*k
#     n1 = C[13][k]
#     n2 = C[rem][need] if 0 <= need <= rem else 0
#     term = (n1 * n2) % MOD
#     ans = ((ans + term) if (k % 2)==1 else (ans - term)) % MOD

# print(ans % MOD)