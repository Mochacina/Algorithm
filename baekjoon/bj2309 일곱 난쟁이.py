l = [int(input()) for _ in range(9)]
l.sort()
s = sum(l)
for i in range(9):
    for j in range(i+1,9):
        if s - l[i] - l[j] == 100:
            for k in range(9):
                if k == i or k == j: continue
                print(l[k])
            exit()