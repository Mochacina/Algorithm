n=int(input())
l=[0,0]
b=[[] for _ in range(2)]
for i in range(2):
    b[i] = input()
    for j in range(n):
        if b[i][j] == 'w': l[i] += 1
l2 = ["Oryang","Its fine","Manners maketh man","Good"]
if l[0] > l[1]: print(l2[0])
if l[0] == l[1] and b[0] != b[1]: print(l2[1])
if l[0] < l[1]: print(l2[2])
if b[0] == b[1]: print(l2[3])