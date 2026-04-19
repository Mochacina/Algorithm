def solution(word):
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]
    ans = 0
    for i in range(len(word)):
        ans += 1 + vowels[word[i]] * weights[i]
    
    return ans