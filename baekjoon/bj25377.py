l=[]
for _ in range(int(input())):
    n,m=map(int,input().split())
    if n <= m: l.append(m)
print(min(l) if len(l) else -1)