MOD = 10007

# nCr 테이블 (파스칼) - 0..52
MAXN = 52
C = [[0]*(MAXN+1) for _ in range(MAXN+1)]
for n in range(MAXN+1):
    C[n][0] = 1
    for r in range(1, n+1):
        C[n][r] = (C[n-1][r-1] + C[n-1][r]) % MOD
for i in C: print(i)

import sys
N = int(sys.stdin.readline().strip())

ans = 0
maxk = min(13, N//4)
for k in range(1, maxk+1):
    n1 = C[13][k]
    n2 = 0
    rem = 52 - 4*k
    need = N - 4*k
    if 0 <= need <= rem:
        n2 = C[rem][need]
    term = (n1 * n2) % MOD
    if (k % 2) == 1:  # k odd => (-1)^{k+1} = +1
        ans = (ans + term) % MOD
    else:             # k even => (-1)^{k+1} = -1
        ans = (ans - term) % MOD

print(ans % MOD)