n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit(): result+=int(i)
    return result

arr = [input() for _ in range(n)]
arr.sort(key = lambda x:(len(x), sum_num(x), x))
for i in arr:
    print(i)