n,m = map(int,input().split())
l = sorted([*map(int,input().split())])
for i in l:
    if i<=m:m+=1
    else: break
print(m)
