n = int(input())
l = sorted([list(map(int,input().split())) for _ in range(n)])
l2 = [i[1] for i in l]

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if l2[i] > l2[j]:
            dp[i] = max(dp[j]+1,dp[i])
            
print(n-max(dp))