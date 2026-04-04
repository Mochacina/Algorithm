r,g,b=map(int,input().split())
r2,g2,b2=r/255,g/255,b/255
k=1-max(r2,g2,b2)
_k=(1-k)
c=(1-r2-k)/_k
m=(1-g2-k)/_k
y=(1-b2-k)/_k
print(c,m,y,k) if k!=1 else print("0 0 0 1")