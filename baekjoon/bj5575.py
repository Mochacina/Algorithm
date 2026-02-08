for _ in range(3):
    a,b,c,d,e,f=map(int,input().split())
    m=a*3600+b*60+c
    n=d*3600+e*60+f
    s=n-m
    print(s//3600,s%3600//60,s%60)