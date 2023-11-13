while 1:
    l = sorted(list(map(int,input().split())))
    if l[0]==0:exit()
    if l[2]>=sum(l[0:2]):print("Invalid")
    elif l[0]*l[2]==l[1]**2:print("Equilateral")
    elif l[0]==l[1] or l[1]==l[2]:print("Isosceles")
    elif l[0]>=1:print("Scalene")