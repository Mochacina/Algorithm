import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dict = {}
for _ in range(n):
    url, pwd = input().split()
    dict[url] = pwd
for _ in range(m):
    print(dict.get(input().strip()))