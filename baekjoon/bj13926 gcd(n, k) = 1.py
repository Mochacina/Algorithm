# 폴라드 로, 밀러 라빈으로 소인수분해하여 인수 목록 구하기
# 구한 인수 목록으로 오일러-피 적용하여 개수 구하기

import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0: return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

def is_prime(n, accuracy=5):
    if n < 2: return 0
    if n in (2, 3): return 1
    if n % 2 == 0 or n % 3 == 0: return 0
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(accuracy):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def factorize(n):
    factors = []
    def recurse(n):
        if is_prime(n):
            factors.append(n)
            return
        factor = pollards_rho(n)
        recurse(factor)
        recurse(n // factor)
    recurse(n)
    return factors

def euler_phi(n):
    if n == 1: return 1
    result = n
    l = set(factorize(n))
    for i in l:
        result -= result // i
    return result

print(euler_phi(int(input())))