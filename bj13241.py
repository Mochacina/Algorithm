# import math
# print(math.lcm(*map(int,input().split())))

a,b=map(int,input().split())
l = [i for i in range(max(a,b),a*b+1,max(a,b))]
for i in l:
    if i%min(a,b)==0: print(i);exit()