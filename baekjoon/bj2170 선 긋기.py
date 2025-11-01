import sys
input = sys.stdin.readline

pools = [tuple(map(int, input().split())) for _ in range(int(input()))]
pools.sort(key=lambda x: (x[0],x[1]))

#print(pools)

mm = 1000000001

sum = 0
start = mm
end = -mm
for x,y in pools:
    if x > end:
        start = x
        end = y
        sum += y-x
    else:
        if y > end: sum += y-end
        start = min(x,start)
        end = max(end,y)
    #print(f"start={start}, end={end}, sum={sum}")
print(sum)