# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# l = list(map(int,input().split()))
# dp = [0] * (a+1)
# ans = ""
# for i in range(b):
#     n,m = map(int,input().split())
#     ans += str(sum(l[n-1:m]))+"\n"
# sys.stdout.write(ans)  

import sys
input = sys.stdin.readline
a,b = map(int,input().split())
l = list(map(int,input().split()))
dp = [0] * (a+1)
for i in range(1,a+1):
    dp[i] = l[i-1] + dp[i-1]
for _ in range(b):
    n,m = map(int,input().split())
    print(dp[m]-dp[n-1])