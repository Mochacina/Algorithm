def solution(operations):
    l = []
    for i in operations:
        n, num = i.split(" ")
        print(i)
        if n == "I": l.append(int(num))
        if n == "D" and len(l):
            if num == '1': del l[(l.index(max(l)))]
            else: del l[l.index(min(l))]
        print(l)
    return [0,0] if not len(l) else [max(l),min(l)]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))