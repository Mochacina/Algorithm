E,S,M=map(int,input().split())
y=1
while not(((y-E)%15==0)and((y-S)%28==0)and((y-M)%19==0)):y+=1
print(y)