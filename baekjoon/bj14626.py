N = input()
sum = 0
mul = 1
for i, n in enumerate(N):
    if n != '*':
        num = int(n)
        num = num if i%2==0 else num*3
        sum += num
    else: mul = 1 if i%2==0 else 3
for i in range(10):
    if (sum+i*mul)%10==0:exit(print(i))