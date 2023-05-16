n,m = map(int, input().split())
cnt = 0
l=""
if(n==0):
    print(0);exit()
for i in range(0,35):
    if(m**i>n):cnt=i;break
for i in range(cnt-1,-1,-1):
    a = n//m**i
    l+=str(a if a<=9 else chr(a+55))
    n=n%(m**i)
print(l)