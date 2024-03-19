# n,m = map(int,input().split())
# l = [*map(int,input().split())]
# l.sort()

# cnt = 0
# i = 0
# while i<n:
#     s = l[i]
#     while i<n and l[i]<=s+m-1:
#         i+=1
#     cnt+=1
# print(cnt)

# n,m = map(int,input().split())
# l = sorted([*map(int,input().split())])
# c=0
# d=-1000
# for i in range(n):
#   if l[i]>d+m-1:c+=1;d=l[i]
# print(c)

n,m=map(int,input().split())
c,d=0,0
for i in sorted([*map(int,input().split())]):
 if i>d:d=i+m-1;c+=1
print(c)