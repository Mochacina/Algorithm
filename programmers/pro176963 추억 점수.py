def solution(name, yearning, photo):
    match = {name[i]:yearning[i] for i in range(len(name))}
    print(match)
    answer = []
    for i in photo:
        l = []
        for k in i:
            try: l.append(match[k])
            except: 0
        answer.append(sum(l))
    print(answer)
    return answer

solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])