l = [0]*26
for _ in range(int(input())):
    l[ord(input()[0])-97] += 1
if max(l)>=5:
    for i in range(len(l)):
        if l[i]>=5: print(chr(i+97),end='')
else: print("PREDAJA")