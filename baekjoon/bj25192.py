l=set()
cnt=0
for _ in range(int(input())):
    n = input()
    if (n == "ENTER"):
        l=set()
    elif n not in l:
        cnt+=1
        l.add(n)
print(cnt)