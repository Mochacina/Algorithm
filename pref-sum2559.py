import sys
input = sys.stdin.readline
a, b = map(int,input().split())
l = list(map(int,input().split()))
temp_sum = sum(l[:b])
dp = [0]*(a-b+1)
dp[0] = temp_sum
for i in range(1, len(dp)):
    dp[i] = dp[i-1] + l[i+b-1] - l[i-1]
print(max(dp))