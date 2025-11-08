cnt=0
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    cnt += (a>999) or (b>1599) or (c>1499) or (1<=d<31)
print(cnt)