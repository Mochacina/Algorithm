# n = int(input())
# l,l2 = list(map(int,input().split())),[]
# l = list(dict.fromkeys(l))
# a = 0
# for i in l:
#     if i > a:
#         a = i
#         l2.append(a)
# print(len(l2))

def longest_increasing_subsequence(A):
    n = len(A)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n = int(input())
l = list(map(int,input().split()))
print(longest_increasing_subsequence(l))