n = int(input())
l = [0,1,2]+[0]*998
for i in range(3,1001):
    l[i] = l[i-1]+l[i-2]
print(l[n]%10007)