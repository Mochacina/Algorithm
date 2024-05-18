from collections import deque
n = int(input())
g = [[] for _ in range(n+1)]
d = [0]*(n+1)
t = [0]*(n+1)

for i in range(1,n+1):
    a,b,*l = map(int,input().split())
    t[i] = a
    for j in l:
        g[j].append(i)
        d[i] += 1

q = deque()
time = [0]*(n+1)
for i in range(1, n+1):
    if not d[i]:
        q.append(i)
        time[i] = t[i]

while q:
    node = q.popleft()
    for i in g[node]:
        d[i] -= 1
        time[i] = max(time[node]+t[i], time[i])
        if d[i] == 0:
            q.append(i)

print(max(time))