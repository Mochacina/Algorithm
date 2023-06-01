import sys
input=sys.stdin.readline
def dq(n,m,c):
    if m==1: return n%c
    x = dq(n,m//2,c)
    return x*x%c if m%2==0 else x*x*n%c
print(dq(*map(int, input().split())))