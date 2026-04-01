a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
sum=0
for i in range(a+1,b+1):
    if i <= 0: sum+=c
    else: sum+=e
    if i == 0: sum+=d
print(sum)