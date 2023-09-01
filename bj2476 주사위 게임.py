l = []
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    if(a==b==c): l.append(10000+a*1000)
    elif(a==b or b==c): l.append(1000+b*100)
    elif(a==c): l.append(1000+a*100)
    else: l.append(max(a,b,c)*100)
print(max(l))