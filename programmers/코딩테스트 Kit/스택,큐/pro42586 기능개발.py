def solution(progresses, speeds):
    day = 1
    level = 0
    answer = []
    while sum(answer) < len(progresses):
        work = 0
        while level < len(progresses) and progresses[level] + speeds[level]*day >= 100:
            work += 1
            level += 1
        if work: answer.append(work)
        day += 1
    return answer

print(solution([93, 30, 55], [1, 30, 5]))