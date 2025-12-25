n=int(input())
l=[*map(int,input().split())]
print(1 if l==sorted(l) else 0)