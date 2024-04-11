# [-1,0,1]
l = [[x,y] for x in [-1,0,1] for y in [-1,0,1] if abs(x+y)==1]
print(l)