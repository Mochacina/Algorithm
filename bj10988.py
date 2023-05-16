n = list(input())
for i in range(len(n)//2):
    if(n[i] != list(reversed(n))[i]):
        print("0");exit()
print("1")