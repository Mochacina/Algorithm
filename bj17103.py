r = int(input())
num = [0]*r
mx = 0
for i in range(r):
    num[i]=int(input())
    mx=max(mx,num[i])
    
l=[1]*(mx+1)
for i in range(2,int(mx**0.5)+1):
    if l[i]:
        for j in range(i+i,mx+1,i):l[j]=0
        
for i in num:
    c=0
    for j in range(2,i//2+1):
        if l[j] and l[i-j]:c+=1
    print(c)