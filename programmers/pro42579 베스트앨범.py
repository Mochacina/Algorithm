def solution(genres, plays):
    l = []
    d = {}
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], 0)+plays[i]
        l.append([i,genres[i],plays[i]])
    l.sort(key=lambda x: (-d[x[1]], -x[2], x[0]))
    n = {}
    answer = []
    for num, gen, play in l:
        n[gen] = n.get(gen,0)+1
        if n[gen] >= 3:
            continue
        else:
            answer.append(num)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))