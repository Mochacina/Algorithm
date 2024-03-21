# N,r,c = map(int,input().split())
# def z(N,r,c,n=0):
#     #print(f"N: {N}, n: {n}")
#     if (N==0): return n
#     half = 2**(N-1)
#     if (r<half and c<half):
#         return z(N-1,r%half,c%half,n)  # Added return statement
#     elif (r<half and c>=half):
#         return z(N-1,r%half,c%half,n+half**2)  # Added return statement
#     elif (r>=half and c<half):
#         return z(N-1,r%half,c%half,n+half**2*2)  # Added return statement
#     else:
#         return z(N-1,r%half,c%half,n+half**2*3)  # Added return statement
# print(z(N,r,c))

N,r,c = map(int,input().split())
def z(N,r,c,n=0):
    if (N==0): return n
    half = 2**(N-1)
    mul = 0
    if (r<half and c<half): pass
    elif (r<half and c>=half): mul = 1
    elif (r>=half and c<half): mul = 2
    else: mul = 3
    return z(N-1,r%half,c%half,n+half**2*mul)
print(z(N,r,c))

# n,r,c=map(int,input().split());
# print(int(f'{c:b}'))
# print(int(f'{r:b}'))
# print(int(f'{c:b}',4))
# print(int(f'{r:b}',4))
# print(int(f'{c:b}',4)+2*int(f'{r:b}',4))