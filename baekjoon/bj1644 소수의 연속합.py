# two pointer
n = int(input())
primes = [1]*(n+1)
for i in range(2, int(n**0.5)+1):
    if primes[i]:
        for j in range(i*i, n+1, i):
            primes[j] = 0

primes = [i for i in range(2, n+1) if primes[i]]

l = 0
r = 0
sum = 0
cnt = 0

while 1:
    if sum >= n:
        if sum == n: cnt += 1
        sum -= primes[l]
        l += 1
    else:
        if r == len(primes): break
        sum += primes[r]
        r += 1

print(cnt)

# pre-sum (시간초과)
# n = int(input())
# primes = [1]*(n+1)
# for i in range(2, int(n**0.5)+1):
#     if primes[i]:
#         for j in range(i*i, n+1, i):
#             primes[j] = 0

# primes = [i for i in range(2, n+1) if primes[i]]
# pre_sum = [0]*(len(primes)+1)
# for i in range(len(primes)):
#     pre_sum[i+1] = pre_sum[i] + primes[i]
    
# cnt = 0
# for i, p in enumerate(pre_sum):
#     pn = p+n
#     for j in pre_sum[i+1:]:
#         if j == pn:
#             cnt += 1
#         elif j > pn:
#             break
# print(cnt)