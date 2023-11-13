# def bc_cq(n, k, memo={}):
#     # 기본 단계: k가 0이거나 k와 n이 같을 경우
#     if k == 0 or k == n: return 1

#     # 이미 계산된 이항 계수인 경우 메모이제이션된 값을 반환
#     if (n, k) in memo:
#         return memo[(n, k)]

#     # 분할 단계: 선택하는 경우와 선택하지 않는 경우로 분할
#     result = bc_cq(n-1, k-1, memo) + bc_cq(n-1, k, memo)

#     # 계산 결과를 메모이제이션
#     memo[(n, k)] = result

#     return result%1000000007

# print(bc_cq(*map(int, input().split())))


n, k = map(int, input().split())
p = 1000000007

def fact(n):
    r = 1
    for i in range (1, n+1): r*=i;r%=p
    return r
    #return n*fact(n-1)%p if n!=1 else 1

def exp(n, k):
    if k == 1: return n
    a = exp(n, k//2)
    b = k%2
    return a*a*(n**b) %p

def bt(n, k):
    if k == 0 or n == k: return 1
    return (fact(n))%p * exp((fact(k))*(fact(n-k)), p-2)%p

print(bt(n,k))