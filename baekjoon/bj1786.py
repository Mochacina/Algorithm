import sys

T = input()
P = input()

def get_pi(p):
    m = len(p)
    pi = [0]*m
    j = 0
    for i in range(1,m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(t, p):
    pi = get_pi(p)
    n,m = len(t),len(p)
    matched = []
    j = 0
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if t[i] == p[j]:
            if j == m-1:
                matched.append(i-m+2)
                j = pi[j]
            else: j+=1
    return matched

result = kmp(T,P)

print(len(result))
print(*result)