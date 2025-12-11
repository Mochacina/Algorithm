n=input()
l=[*map(int,input().split())]
y=sum([(1+i//30) for i in l])*10
m=sum([(1+i//60) for i in l])*15
if y<m: print(f"Y {y}")
elif y>m: print(f"M {m}")
else: print(f"Y M {y}")