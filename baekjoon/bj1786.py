import sys

T = input()
P = input()

def get_pi(pattern):
    m = len(pattern)
    pi = [0]*m
    j = 0
    for i in range(1,m):
        while n > 0 and pattern[i] != pattern[j]: n = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(text, pattern):
    pi = get_pi(pattern)
    n,m = len(text),len(pattern)
    matched = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        if text[i] == pattern[j]:
            if j == m-1:
                matched.append(i-m+2)
                j = pi[j]
            else: j+=1
    return matched

result = kmp(T,P)

print(len(result))
print(*result)