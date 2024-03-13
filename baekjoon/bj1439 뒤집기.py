str = input()
cnt = 0
n = str[0]

for i in range(1, len(str)):
    if n != str[i]:
        cnt += 1
        n = str[i]

print((cnt+1)//2)