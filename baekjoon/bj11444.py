def c_mul(A,B):
    return [[sum([A[i][k]*B[k][j] for k in range(len(B))])%p for j in range(len(B[0]))]for i in range(len(A))]
def c_dq(A,c):
    if c==1: return A
    l = c_dq(A,c//2)
    return c_mul(l,l) if c%2==0 else c_mul(c_mul(l,l),A)

n = int(input())
p = 1000000007
if n<3: print(1)
else: print(c_mul(c_dq([[1,1],[1,0]],n-2),[[1],[1]])[0][0]%p)