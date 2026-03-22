n=int(input())
l=[*map(int,input().split())]
l[0]=[-1,1][l[0]]
for i in range(1,n):
    l[i] = l[i-1]+[-1,1][l[i]]
print(sum(l))