import math
h,w,n,m = map(int,input().split())
x = math.ceil(h/(n+1))
y = math.ceil(w/(m+1))
print(x*y)