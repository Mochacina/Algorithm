n = int(input())
stack,ans = [],[]
ptr = 1
for i in range(n):
    num = int(input())
    while ptr<=num:
        stack.append(ptr)
        ans.append('+')
        ptr+=1
    if stack[-1] == num:
        ans.append('-')
        stack.pop()
    else:
        print("NO")
        exit()
[print(i) for i in ans]