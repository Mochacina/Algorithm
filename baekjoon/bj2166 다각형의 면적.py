n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
a = 0
for i in range(n):
    x1, y1 = l[i]
    x2, y2 = l[(i+1)%n]
    a += x1*y2 - y1*x2
print(abs(a)/2)