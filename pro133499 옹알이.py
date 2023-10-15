def solution(babbling):
    answer = 0
    for word1 in babbling:
        word = word1
        backword = ""
        while word:
            if len(word) > 2 and word[0:3] == "aya" and word[0:3] != backword:
                word = word[3:]
                backword = "aya"
            elif len(word) > 1 and word[0:2] == "ye" and word[0:2] != backword:
                word = word[2:]
                backword = "ye"
            elif len(word) > 2 and word[0:3] == "woo" and word[0:3] != backword:
                word = word[3:]
                backword = "woo"
            elif len(word) > 1 and word[0:2] == "ma" and word[0:2] != backword:
                word = word[2:]
                backword = "ma"
            elif len(word) > 0:
                answer -= 1
                break
        answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]		
print(solution(babbling))