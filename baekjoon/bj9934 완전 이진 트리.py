from collections import deque
num = int(input())
tree = list(map(int, input().split(" ")))
dq = deque([tree])
l = []
while dq:
    node = dq.popleft()
    n = len(node)//2
    l.append(node[n])
    if n: 
        dq.append(node[0:n])
        dq.append(node[n+1:])
for i in [2**i for i in range(num)]: print(" ".join(map(str, l[i-1:i*2-1])))