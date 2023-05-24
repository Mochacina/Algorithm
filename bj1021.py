from collections import deque
cnt = 0
n,m = map(int, input().split())
d = deque([i for i in range(1,n+1)])
l = deque(list(map(int, input().split())))
while len(l):
    if d[0] == l[0]:
        d.popleft()
        l.popleft()
    else:
        cnt+=1
        if d.index(l[0]) <= len(d)//2:
            d.append(d.popleft())
        else:
            d.appendleft(d.pop())
print(cnt)