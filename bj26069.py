dic = {"ChongChong":1}
for _ in range(int(input())):
    a,b = input().split()
    for i in [a,b]:
        if(dic.get(i)==None):dic[i]=0
    for i in [a,b]:
        if(dic.get(i)==1):
            dic[a]=1;dic[b]=1;break
print(sum(dic.values()))