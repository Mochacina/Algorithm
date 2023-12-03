N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(M)]
min_1=min([i[1]for i in l])
min_6=min(min([i[0]for i in l]),min_1*6)
print(min_6*(N//6) + min(min_6,min_1*(N%6)))