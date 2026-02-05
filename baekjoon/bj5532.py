import math
L,a,b,c,d=map(int,(input()for _ in range(5)))
a1=math.ceil((a/c))
b1=math.ceil((b/d))
print(L-max(a1,b1))