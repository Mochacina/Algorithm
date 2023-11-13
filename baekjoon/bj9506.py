while(True):
    n = int(input())
    if(n==-1): break
    l = []
    for i in range(1,n//2+1):
        if(n%i==0): l.append(i)
    if(sum(l)==n):
        print(f"{n} = " + " + ".join(map(str, l)))
    else: print(f"{n} is NOT perfect.")