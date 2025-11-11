p,m,c = map(int,input().split())
X=int(input())
M=10**9
for i in range(1,p+1):
    for j in range(1,m+1):
        for k in range(1,c+1):
            M = min(M,abs((i+j)*(j+k)-X))
print(M)