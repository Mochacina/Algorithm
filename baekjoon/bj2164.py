from collections import deque
l = deque([i+1 for i in range(int(input()))])
while len(l)>1:
    l.popleft()
    l.append(l.popleft())
print(l[0])