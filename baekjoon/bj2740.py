n1,m1 = map(int,input().split())
l1 = [list(map(int,input().split())) for _ in range(n1)]
n2,m2 = map(int,input().split())
l2 = [list(map(int,input().split())) for _ in range(n2)]
l = [[0]*m2 for _ in range(n1)]
for i in range(n1):
    for j in range(m2):
        s = sum([l1[i][k]*l2[k][j] for k in range(m1)])
        l[i][j] = s
for i in l: print(*i)