a,b=map(int,input().split())
n,m=map(int,input().split())
top=min(b,n+m)
bottom=max(a,n-m)
sum=(top-bottom)+1
print(sum if sum >= 0 else "IMPOSSIBLE")