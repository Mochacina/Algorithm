from collections import deque
n = int(input())
q = deque(enumerate(map(int,input().split())))
ans=[]

while q:
    idx,num = q.popleft()
    ans.append(idx+1)
    q.rotate(-(num-1)) if num>0 else q.rotate(-num)
print(*map(str,ans))