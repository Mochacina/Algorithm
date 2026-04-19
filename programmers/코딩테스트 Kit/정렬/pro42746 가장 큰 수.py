def solution(numbers):
    a = ''.join(map(str, sorted(numbers,key=lambda x:str(x)*4,reverse=True)))
    return a if a[0] != '0' else 0

print(solution([6, 10, 2]))