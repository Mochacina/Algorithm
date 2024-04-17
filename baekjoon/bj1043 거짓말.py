n,m = map(int, input().split())
_, *true = map(int, input().split())
pa = [i if i not in true else 0 for i in range(n+1)]
def find(x):
    if x != pa[x]:
        pa[x] = find(pa[x])
    return pa[x]
parties = [[]for _ in range(m)]
for j in range(m):
    cnt, *party = map(int, input().split())
    parties[j] = party
    for i in range(cnt-1):
        l,r = find(party[i]), find(party[i+1])
        if l < r: pa[r] = l
        else: pa[l] = r
cnt = 0
for party in parties:  
    if find(party[0]) == 0:
        continue
    cnt += 1
print(cnt)

# n,m = map(int, input().split())
# _, *true = map(int, input().split())
# true_l = [0 if i not in true else 1 for i in range(n+1)]
# #print(true_l)
# cnt = 0
# parties = []
# for _ in range(m):
#     _, *party = map(int, input().split())
#     parties.append(party)
#     if max([true_l[mem] for mem in party]):
#         for mem in party:
#             true_l[mem] = 1
# #print(true_l)
# for pt in parties:
#     for member in pt:
#         if true_l[member]: break
#     else: cnt+=1
# print(cnt)