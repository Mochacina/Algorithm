from collections import deque
import sys
l = deque()
for _ in range(int(input())):
    try:
        a = sys.stdin.readline().rstrip().split()
    except:
        pass
    if (a[0]=="push_front"):
        l.appendleft(a[1])
    elif (a[0]=="push_back"):
        l.append(a[1])
    elif (a[0]=="pop_front"):
        print(l.popleft() if len(l)>0 else -1)
    elif (a[0]=="pop_back"):
        print(l.pop() if len(l)>0 else -1)
    elif (a[0]=="size"):
        print(len(l))
    elif (a[0]=="empty"):
        print(0 if len(l)>0 else 1)
    elif (a[0]=="front"):
        print(l[0] if len(l)>0 else -1)
    elif (a[0]=="back"):
        print(l[-1] if len(l)>0 else -1)