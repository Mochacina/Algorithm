l = list(map(int,input().split()))
sum = 0
for _ in range(int(input())):
    a,b,c = map(float,input().split())
    a = int(a)
    if b >= 2.0 and c >= 17:
        sum += l[a]
print(sum)