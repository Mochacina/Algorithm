def solution(sizes):
    min_n = []
    max_n = []
    for args in sizes:
        mi = min(args)
        mx = max(args)
        min_n.append(mi)
        max_n.append(mx)
    
    return max(max_n)*max(min_n)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))