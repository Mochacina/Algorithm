# n = int(input())
# for i in range(n):
#     l = input()
#     depth = 1
#     arg = '('
#     for j in range(len(l)):
#         if j==0:
#             if l[j]=='(':
#                 depth=1
#                 arg = '('
#             else:
#                 depth=-51
#                 continue
#         else:
#             if arg=='(' and l[j]==arg:depth+=1
#             elif arg==')' and l[j]==arg:depth-=1
#             else:
#                 if arg=='(':
#                     arg=')'
#                     depth-=1
#                 else:
#                     arg='('
#                     depth+=1
#     print("YES" if depth==0 else "NO")


n = int(input())
for i in range(n):
    l = input()
    depth = 0
    for j in range(len(l)):
        if l[0]==')' or l[-1]=='(' or depth<=-1:
            depth=100
            break
        if l[j]=='(':depth+=1
        else:depth-=1
    print("YES" if depth==0 else "NO")