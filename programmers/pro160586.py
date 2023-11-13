def solution(keymap, targets):
    answer = []
    for target in targets:
        sum = 0
        for i in target:
            n = 101
            for key in keymap:
                if i in key: n = min(n,key.index(i)+1)
            if n == 101:
                sum = -1
                break
            else: sum += n
        answer.append(sum)
    return answer

keymap = ["AGZ", "BSSS"]	
targets = ["ASA","BGZ"]	

print(solution(keymap, targets))