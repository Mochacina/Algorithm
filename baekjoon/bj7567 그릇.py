n = input()
d = ''
sum = 0
for i in n:
    sum += 5 if d==i else 10
    d=i
print(sum)