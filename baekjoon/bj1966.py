# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     l = list(map(int,input().split()))
#     print(l)

from collections import deque
for _ in range(int(input())):
    a,p = map(int,input().split())
    l = deque(list(map(int,input().split())))
    n=1
    while True:
        #print("p:", p)
        #print(l)
        if(l[0]==max(l)):
            if(p==0):print(n);break
            else:
                l.popleft()
                p-=1;n+=1
        else:
            l.append(l.popleft())
            p=len(l)-1 if(p==0) else p-1