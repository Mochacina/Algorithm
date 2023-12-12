l=sorted([int(input()) for _ in range(int(input()))])
sum = 0
for n,i in enumerate(l):sum+=abs(n+1-i)
print(sum)