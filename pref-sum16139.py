import sys
input = sys.stdin.readline
l = input()
n = int(input())
dp = [[0]*(len(l)+1) for _ in range(ord('z')+1)]
for i in range(ord('a'),ord('z')+1):
    for j in range(1,len(l)+1):
        dp[i][j] = dp[i][j-1]+1 if l[j-1]==chr(i) else dp[i][j-1]
for i in range(n):
    a,b,c = input().split()
    print(dp[ord(a)][int(c)+1]-dp[ord(a)][int(b)])