n, s = map(int,input().split())
l = list(map(int,input().split()))

list = []
answer = []

def dfs(a):
    if len(list) != 0 and sum(l[i] for i in list) == s:
        #print(list)
        if set(list) not in answer:
            answer.append(set(list))
        return
    for i in range(a,n):
        if i not in list:
            list.append(i)
            dfs(a+1)
            list.pop()

dfs(0)
print(len(answer))

    
# for i in range(n): # 숫자 몇개 고를지 for문
#     buf = []
#     for _ in range(i):
#         for j in range(n):
            