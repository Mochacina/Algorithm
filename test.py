n = 5/2
print(n)

print(n.is_integer())

di = [(x-1,y-1) for x in range(3) for y in range(3) if x!=y and x+y!=2]
print(di)

l = [1]
print(l[:-1])

l = []
for i in range(5):
    l += [i]

print(l)