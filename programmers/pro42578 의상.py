def solution(clothes):
    counts = {}
    for name, type in clothes:
        counts[type] = counts.get(type, 0)+1
    result = 1
    for c in counts.values():
        result *= (c+1)
    return result - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))