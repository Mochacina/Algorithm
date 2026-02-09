for i in range(int(input())):
    if i > 0: print()
    l = list(map(int,input().split()))
    print('Denominations:',*l[1:])
    gb = 0
    for i in range(2,len(l)):
        if l[i] < l[i-1]*2: gb = 1;break
    print(f"{['Good','Bad'][gb]} coin denominations!")