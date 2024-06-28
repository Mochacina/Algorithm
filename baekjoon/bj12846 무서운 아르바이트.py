n = int(input())
l = [0]+[*map(int,input().split())]+[0]
s = [0]
m = 0
for i in range(1,n+2):
    while s and l[s[-1]] > l[i]:
        num = s.pop()
        m = max(m,(i-s[-1]-1)*l[num])
    s.append(i)
print(m)