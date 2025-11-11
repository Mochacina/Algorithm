n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[[] for _ in range(m+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if a[i] == b[j]:
            dp[i][j] = [a[i]] + dp[i+1][j+1]
        
        candidates = [dp[i][j], dp[i+1][j], dp[i][j+1]]
        dp[i][j] = max(candidates)

result = dp[0][0]
print(len(result))
if result:
    print(*result)