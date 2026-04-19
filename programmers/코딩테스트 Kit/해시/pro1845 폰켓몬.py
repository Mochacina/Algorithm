def solution(nums):
    dict = {}
    for arg in nums:
        dict[arg] = dict.get(arg,0)+1
    return min(len([*dict.keys()]),len(nums)/2)

print(solution([3,3,3,2,2,4]))