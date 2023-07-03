d = {'-1':0, '0':0, '1':0}
def div_conq(n,l):
    color = l[0][0]
    f = True
    for i in range(n):
        for j in range(n):
            if l[i][j]!=color: f=False
    if f or n==1: d[color]+=1
    else:
        h=n//3
        for i in range(3):
            for j in range(3):
                div_conq(h,[r[h*i:h*(i+1)]for r in l[h*j:h*(j+1)]])
n = int(input())
l = [list(input().split()) for _ in range(n)]
div_conq(n,l)
for i in d.items(): print(i[1])


        # div_conq(h,[r[:h]for r in l[:h]])
        # div_conq(h,[r[:h]for r in l[h:h*2]])
        # div_conq(h,[r[:h]for r in l[h*2:]])
        # div_conq(h,[r[h:h*2]for r in l[:h]])
        # div_conq(h,[r[h:h*2]for r in l[h:h*2]])
        # div_conq(h,[r[h:h*2]for r in l[h*2:]])
        # div_conq(h,[r[h*2:]for r in l[:h]])
        # div_conq(h,[r[h*2:]for r in l[h:h*2]])
        # div_conq(h,[r[h*2:]for r in l[h*2:]])