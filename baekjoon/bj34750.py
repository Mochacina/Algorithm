l=[5,10,15,20]
n=int(input())
m=0
if n > 99999: m+=1
if n > 499999: m+=1
if n > 999999: m+=1
print(n*l[m]//100,n*(100-l[m])//100)