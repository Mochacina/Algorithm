cnt = [0,0]
def div_conq(n,l):
    color = l[0][0]
    f = True
    for i in range(n):
        for j in range(n):
            if l[i][j]!=color:
                f=False
    if f or n==1:
        cnt[color]+=1
    else:
        h=n//2
        div_conq(h,[r[h:]for r in l[h:]])
        div_conq(h,[r[:h]for r in l[:h]])
        div_conq(h,[r[h:]for r in l[:h]])
        div_conq(h,[r[:h]for r in l[h:]])
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
div_conq(n,l)
for i in cnt:
    print(i)