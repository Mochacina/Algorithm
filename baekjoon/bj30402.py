l = [input().split(' ') for _ in range(15)]
d = {'w':"chunbae",'b':"nabi",'g':"yeongcheol"}
for i in l:
    for k in i:
        if k in d: exit(print(d[k]))