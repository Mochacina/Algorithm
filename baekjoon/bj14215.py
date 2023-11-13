a,b,c = sorted(map(int,input().split()))
print(a+b+c if (c<a+b) else (a+b)*2-1)