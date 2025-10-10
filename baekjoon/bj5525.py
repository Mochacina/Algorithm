import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().strip()

ans = 0
count = 0
i = 0

while i < m - 2:
    if s[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            ans += 1
            count -= 1
    else:
        i += 1
        count = 0
            
print(ans)