a = input()
b = input()
l = [[0] * (len(b)+1) for i in range(len(a)+1)]
for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i == 0 or j == 0:
            l[i][j] = 0
        elif a[i - 1] == b[j - 1]:
            l[i][j] = l[i - 1][j - 1] + 1
        else:
            l[i][j] = max(l[i - 1][j], l[i][j - 1])
print(max([max(i) for i in l]))