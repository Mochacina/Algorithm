l = [0]*5;n = 0
for i in range(5):
    l[i] = input()
    n = max(len(l[i]),n)
for x in range(n):
    for y in range(5):
        try:print(l[y][x],end="")
        except:continue