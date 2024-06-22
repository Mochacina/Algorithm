n = 5/2
print(n)

print(n.is_integer())

di = [(x-1,y-1) for x in range(3) for y in range(3) if x!=y and x+y!=2]
print(di)

l = [1,2,3]
print(l[:-1])

l = []
for i in range(5):
    l += [i]

print(l)

l = []
l += "hello"

print(l)

visited = [[[0]*(1<<6) for _ in range(2)] for _ in range(2)]

print(visited)
#print(ord('A'), chr(60))

for i in range(n:=ord('A'), n+26, 1):
    print(chr(i))

print(1<<2)

for i in range(10):
    print(((i==9)<<1) | (i==0)) 

print([*"1 4 7 13 25 37 46 49 52 45 33 21".split(' ')])

print([*range(10)])

print(1e3)

l = [1]*5
print(l)
l = [0,0]+l
print(l)