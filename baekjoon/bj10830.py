def c_mul(A,B,c):
    return [[sum([A[i][k]*B[k][j]for k in range(c)])%1000 for j in range(c)]for i in range(c)]
def c_dq(A,b,c):
    if c==1:return A
    if c%2==0:
        l2 = c_dq(A,b,c//2)
        return c_mul(l2,l2,b)
    else:
        l2 = c_dq(A,b,(c-1)//2)
        return c_mul(c_mul(l2,l2,b),A,b)
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
for i in c_dq(l,n,m): print(*[j%1000 for j in i])