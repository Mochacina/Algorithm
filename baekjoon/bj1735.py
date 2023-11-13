import math
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
n=math.lcm(a2,b2)
m=int(a1*n/a2+b1*n/b2)
k=math.gcd(n,m)
print(f"{m/k:.0f} {n/k:.0f}")