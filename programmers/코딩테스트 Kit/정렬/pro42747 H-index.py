def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
    return len(citations)
    
    # n = len(citations)
    # l = sorted(citations, reverse=True)
    # answer = 0
    # for i, cnt in enumerate(l):
    #     if (n-i >= cnt) and (n-i-1 <= cnt):
    #         answer = max(answer, cnt)
    # return answer

print(solution([3, 0, 6, 1, 5]))