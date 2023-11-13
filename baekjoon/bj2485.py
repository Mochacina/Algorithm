import math
n=0;f=0;l=[];sum=0
for i in range(int(input())):
    if(i!=0):
        f=n
        n=int(input())
        l.append(n-f)
    else:
        n=int(input())
n=math.gcd(*l)
for i in l: sum+= i//n-1
print(sum)