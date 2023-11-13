l = [[] for _ in range(int(input())+1)]
a,b = map(int,input().split())
for _ in range(int(input())):
    n,m = map(int,input().split())
    l[n].append(m)
    l[m].append(n)
queue = [(a,0)]
visited = []

while queue:
    node,count = queue.pop()
    if node not in visited:
        visited.append(node)
        for i in l[node]:
            queue.append((i,count+1))
            if i == b: print(count+1);exit()
print(-1)

