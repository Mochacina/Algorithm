def solution(number):
    l = []
    n = len(number)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and i!=k and sum([number[i], number[j], number[k]])==0:
                    if {i,j,k} not in l:
                        l.append({i,j,k})
    return len(l)

number = [-3, -2, -1, 0, 1, 2, 3]		
print(solution(number))