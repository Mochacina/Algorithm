n = int(input())
l = [0]+[*map(int, input().split())]
ans = 500
for i in range(1,n):
    for j in range(i+1,n+1):
        d = (l[j]-l[i]) / (j-i)
        cnt = 0
        if d.is_integer():
            start = l[i]-i*d
            for k in range(1, n+1):
                if l[k] != start + k*d:
                    cnt += 1
            ans = min(ans, cnt)
print(ans)