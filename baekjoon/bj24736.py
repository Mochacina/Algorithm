l=[6,3,2,1,2]
a=[l[i]*n for i,n in enumerate(map(int,input().split()))]
b=[l[i]*n for i,n in enumerate(map(int,input().split()))]
print(sum(a),sum(b))