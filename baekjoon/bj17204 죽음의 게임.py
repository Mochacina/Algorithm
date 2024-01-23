n,m = map(int, input().split())
l = [int(input()) for _ in range(n)]
visited=[0]*n
t=0;d=0;
while 1:
    if not visited[d]:visited[d]=1
    else:
        print(-1)
        break
    if(d==m):
        print(t)
        break
    d=l[d]
    t+=1