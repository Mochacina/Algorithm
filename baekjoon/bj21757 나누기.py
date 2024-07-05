p=input
n,s=int(p()),0
l=[s:=s+i for i in[*map(int,p().split())]]
d=[1,0,0,0]
for i in range(n-1):
 for j in[3,2,1]:
  if l[i]==s//4*j:d[j]+=d[j-1]
print([d[3],0][s%4>0])