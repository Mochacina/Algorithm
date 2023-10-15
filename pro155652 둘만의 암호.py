from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    
    alphabet = list(ascii_lowercase)
    for word in skip:
        alphabet.remove(word)
    for word in s:
        answer += alphabet[(alphabet.index(word)+index)%len(alphabet)]
        
    return answer

s = "aukks"	
skip = "wbqd"
index = 5

print(f"result: {solution(s,skip,index)}")