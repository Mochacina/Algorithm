a,b=map(int,input().split())
l=list(map(int,input().split()))
n,dp=0,[0]*b
dp[0]=1
for i in range(a):n+=l[i];dp[n%b] += 1
print(sum([i*(i-1)//2 for i in dp]))



# pref_sum = [0]*(sum)
# n = 0
# for i in range(1,a+1): # 1~5
#     for j in range(i): # 0, 0~1, 0~2, 0~3, 0~4
#         pref_sum[n] = dp[i]-dp[j]
#         n+=1
# print(pref_sum.count())