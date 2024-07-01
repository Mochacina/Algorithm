# N,K=map(int,input().split())
# prev = [1]*(N+1)
# curr = [1]*(N+1)
# for i in range(1,K):
#     for j in range(1,N+1):
#         if i > 0 and j > 0:
#             curr[j] = curr[j-1] + prev[j]
#     prev, curr = curr, prev
# print(prev[N]%1000000000)

# 이항 계수 사용
import math
N,K=map(int,input().split())
print(math.comb(N+K-1,K-1)%10**9)

# 이항 계수 직접 계산
# import sys
# I = sys.stdin.readline
# mod = 1_000_000_000

# n,k = map(int,I().split())
# m = n+k-1
# if 2*n>m: n = m-n

# arr = [1]
# for i in range(1,m+1):
#     arr.append(1)
#     for j in range(i-1,0,-1):
#         arr[j] += arr[j-1]
#         arr[j] %= mod
# print(arr[n])