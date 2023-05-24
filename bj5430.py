from collections import deque
import sys

for _ in range(int(input())):
    flag = True
    n = input()
    c = int(input())
    r = 0
    try:
        l = deque(list(input().rstrip()[1:-1].split(',')))
    except:
        l = deque([])
    if "" in l:l.pop()
    for i in range(len(n)):
        if(n[i]=="R"):r+=1
        elif(n[i]=="D"):
            if(len(l)<1):
                print("error");flag=False
                break;
            else:
                if r%2==0:l.popleft()
                else:l.pop()
    if flag:
        if r%2==0:
            print("[" + ",".join(l) + "]")
        else:
            l.reverse()
            print("[" + ",".join(l) + "]")

        # print("[",end="")
        # for j in range(len(i)):
        #     if j != len(i)-1: print(l[j],end=",")
        #     else: print(i[j],end="]\n")