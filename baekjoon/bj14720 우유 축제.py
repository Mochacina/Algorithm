int(input())
l=map(int,input().split())
n=0;cnt=0
for i in l:
    if i == n:
        cnt+=1
        n=(n+1)%3
print(cnt)