def solution(n):
    bin1 = len([i for i in bin(n)[2:] if i == "1"])
    for i in range(n+1, 10**6+1):
        if bin1 == len([i for i in bin(i)[2:] if i == "1"]): return i

n = 78
print(solution(n))