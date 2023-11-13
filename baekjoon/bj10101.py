l=[]
for i in range(3):l.append(int(input()))
if sum(l)!=180:print("Error");exit()
l=sorted(l)
if l[0]==l[2]:print("Equilateral");exit()
if l[0]==l[1] or l[1]==l[2]:print("Isosceles")
else: print("Scalene")