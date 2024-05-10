k,n=map(int,input().split())
l=[int(input())for _ in range(k)]
print(''.join(map(str,sorted(l+[max(l)]*(n-k),key=lambda x:str(x)*10,reverse=True))))