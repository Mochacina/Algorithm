n = int(input())
l = list(map(int,input().split()))
l2 = list(reversed(l))

dp1 = [1]*n
dp2 = [1]*n

for i in range(1,n):
    for j in range(i):
        if l[i] > l[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if l2[i] > l2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = list(reversed(dp2))

a = [dp1[i]+dp2[i]-1 for i in range(n)]

print(max(a))