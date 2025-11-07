import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    score = 0
    s=[100,90,95,90,80]
    if a in [1,2]: score+=1
    if d >= 50: score+=1
    if s[a-1] > b*3 and s[a-1] > c*3: score+=0.5
    if b < 22 or c < 22: score+=0.5
    print('YES' if score > 2 else 'NO')