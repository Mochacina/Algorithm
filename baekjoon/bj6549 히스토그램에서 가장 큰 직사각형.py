while (data:=[*map(int,input().split())])[0]:
    l = [0]+data[1:]+[0]
    s = [0]
    m = 0
    for i in range(1,data[0]+2):
        while s and l[s[-1]] > l[i]:
            p = s.pop()
            m = max(m,l[p]*(i-s[-1]-1))
        s.append(i)
    print(m)