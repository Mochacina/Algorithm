p=input;r=range
for _ in r(int(p())):
 n=int(p())+1
 l=[[*map(int,p().split())]for _ in r(n+1)]
 v=[0]+[1]*n;s=[0]
 while s:
  e=s.pop();x,y=l[e]
  for c,i in enumerate(l):
   if v[c]:
    a,b=i
    if abs(x-a)+abs(y-b)<=1000:s.append(c);v[c]=0
 print(["happy","sad"][v[n]])