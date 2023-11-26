# a,b=0,0
# l = [[0,0,0]for _ in range(41)]

# def fib(n):
#     global a,b
#     if n==0:
#         a+=1
#         return 0
#     if n==1:
#         b+=1
#         return 1
#     else:
#         if not l[n][0]:
#             print(m:=fib(n-2)+fib(n-1))
#             l[n][0]=m
#             l[n][1]=a
#             l[n][2]=b
#         else:
#             a+=l[n][1]
#             b+=l[n][2]
#         return l[n][0]

# for _ in range(int(input())):
#     a,b=0,0
#     fib(n:=int(input()))
#     print(l)
#     print(a,b)

l = [0,1]+[0]*39
def fib(n):
    if n==0: return 0
    elif not l[n]:l[n]=fib(n-2)+fib(n-1)
    return l[n]
for _ in range(int(input())):
    a,b=0,0
    fib(n:=int(input()))
    if n==0:print("1 0")
    else: print(l[n-1], l[n])