n = int(input())
if (n % 5) % 2 == 0:
    print(n//5 + (n % 5)//2)
elif (n % 5) % 2 == 1 and n > 5:
    print((n-5)//5 + ((n % 5)+5)//2)
else: print(-1)