from math import ceil
n = int(input())
l = list(map(int, input().split()))
t,p = map(int, input().split())
print(sum([ceil(i/t) for i in l]))
print(n//p,n%p)