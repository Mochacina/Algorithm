num=[380,425,450,495,570,590,620,781]
colors=['Red','Orange','Yellow','Green','Blue','Indigo','Violet']
m = int(input())
for i in range(7):
    if num[i] <= m < num[i+1]:
        print(colors[::-1][i])