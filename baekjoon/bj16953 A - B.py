# A,B = map(int,input().split())
# cnt = 1
# while A<B:
#     if B%10 == 1:
#         B//=10
#         cnt+=1
#     elif B%2 == 0:
#         B//=2
#         cnt+=1
#     else:
#         break
    
# if A==B:
#     print(cnt)
# else:
#     print(-1)

from collections import deque
a,b = map(int,input().split())
l = deque()
l.append((a,1))
while l:
    n,m = l.popleft()
    if n==b:print(m);exit()
    if n*2 <= b:l.append((n*2,m+1))
    if (n1:=int(str(n)+'1')) <= b:l.append((n1,m+1))
print(-1)