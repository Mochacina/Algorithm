n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
l = sorted(l, key=lambda x : (x[1],x[0]))
cnt, n = 0, 0
for i in l:
    if i[0] >= n:
        cnt+=1
        n=i[1]
print(cnt)