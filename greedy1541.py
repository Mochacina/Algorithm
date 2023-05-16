l = input()
l1,l2 = [],[]

num = ''
for i in l:
    if i=='+'or i=='-':
        if i=='+': l2.append('+')
        else: l2.append('-')
        l1.append(int(num))
        num = ''
    else:
        num = num+i
l1.append(int(num))

n1,n2 = l1[-1],l1[0]

for i in range(len(l2)-1,-1,-1):
    if i==0 and l2[i] == '+':
        n2 += n1
    if l2[i] == '-':
        n2 -= n1
        n1 = 0
    n1 += l1[i]
    
print(n2)