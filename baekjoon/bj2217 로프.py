N = int(input())
l = sorted([int(input()) for _ in range(N)])[::-1]
m = 0
for i in range(N):
    m = max(l[i]*(i+1), m)
print(m)