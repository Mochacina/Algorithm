# ���� ���� ����� ���� ������ n���� ��ġ�� ���� �������� �������� ������.
# �� ������ �ִ� k������ ���� �� �ִ� ��� ������ �ִ� log k���� �������� ������ �� �ִ�.

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