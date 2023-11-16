n,m,b = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
time = 0
while 1:
    max_l = max([max(i) for i in l])
    sum_l = sum([sum(i) for i in l])