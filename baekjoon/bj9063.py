min_x,min_y,max_x,max_y = 10000,10000,-10000,-10000
for _ in range(int(input())):
    n,m = map(int, input().split())
    min_x = min(n,min_x)
    min_y = min(m,min_y)
    max_x = max(n,max_x)
    max_y = max(m,max_y)
print(abs(max_x-min_x)*abs(max_y-min_y))