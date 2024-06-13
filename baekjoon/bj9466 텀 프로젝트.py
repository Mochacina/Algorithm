# import sys
# i = sys.stdin.readline
# for _ in ' '*int(i()):
#     n = int(i())
#     l = [0]+[*map(int,i().split())]
#     members = [0]*(n+1)
#     cnt = 0
#     for a in range(1,n+1):
#         if members[a]: continue
#         start = a
#         node = l[a]
#         member = set([a])
#         while node not in member:
#             member.add(node)
#             node = l[node]
#         if node == start:
#             for b in member: members[b] = 1
#     print(n-sum(members))

i = input
def dfs(n,m=[]):
    v[n] = 1
    m.append(n)
    node = l[n]
    dfs(node,m)

for _ in ' '*int(i()):
    n = int(i())
    l = [0]+[*map(int,i().split())]
    v = [0]*(n+1)
    cnt = 0
    for a in range(1,n+1):
        if not v[a]:
            print(dfs(a))