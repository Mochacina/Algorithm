def qt(n,l):
    color = l[0][0]
    f = True
    for i in range(n):
        for j in range(n):
            if l[i][j]!=color:
                f=False
    if f or n==1:
        print(color,end="")
    else:
        h=n//2
        print(end="(")
        qt(h,[r[:h]for r in l[:h]])
        qt(h,[r[h:]for r in l[:h]])
        qt(h,[r[:h]for r in l[h:]])
        qt(h,[r[h:]for r in l[h:]])
        print(end=")")
n = int(input())
l = []
for _ in range(n):
    row = input()
    l.append([int(row[i]) for i in range(n)])
qt(n,l)