n = int(input())
l,cnt = [0]*n,0
def q_check(x):
    for i in range(x):
        if l[x]==l[i] or abs(l[x]-l[i])==abs(x-i): return False
    return True
def dfs(x):
    global cnt
    if x==n:
        cnt+=1;return
    for i in range(n):
        l[x]=i
        if q_check(x):
            dfs(x+1)
dfs(0)
print(cnt)