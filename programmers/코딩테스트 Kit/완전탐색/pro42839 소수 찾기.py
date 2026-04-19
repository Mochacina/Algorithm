from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            nums.add(int("".join(p)))
    ans = 0
    for n in nums:
        if is_prime(n):
            ans += 1
        
    return ans