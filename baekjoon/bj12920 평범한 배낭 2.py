# 이진 분할 기법을 통해 물건을 n배의 가치를 지닌 여러개의 물건으로 나눈다.
# 각 물건을 최대 k개까지 넣을 수 있는 경우 물건을 최대 log k개의 물건으로 분할할 수 있다.

# n,m = map(int,input().split())
# items = []
# for _ in range(n):
#     v,c,k = map(int, input().split())
#     cnt=1
#     while cnt <= k:
#         items.append((v*cnt, c*cnt))
#         k -= cnt
#         cnt *= 2
#     if k: items.append((v*k, c*k))

# dp = [0]*(m+1)

# for weight, value in items:
#     for j in range(m, weight - 1, -1):
#         dp[j] = max(dp[j], dp[j - weight] + value)

# print(dp[m])

n,m,*l=map(int,open(0).read().split())
i=[]
for j in range(0,n*3,3):
 v,c,k,t=l[j],l[j+1],l[j+2],1
 while t<=k:i.append((v*t,c*t));k-=t;t*=2
 if k:i.append((v*k,c*k))
d=-~m*[0]
for w,v in i:
 for j in range(m,w-1,-1):d[j]=max(d[j],d[j-w]+v)
print(d[m])

# for weight, value in items:
#     for j in range(m, weight - 1, -1):
#         dp[j] = max(dp[j], dp[j - weight] + value)

# print(dp[m])