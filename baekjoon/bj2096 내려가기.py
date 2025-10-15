import sys
input = sys.stdin.readline

n = int(input())
prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for _ in range(n-1):
    a = list(map(int, input().split()))
    curr_max = [0]*3
    curr_min = [0]*3
    
    curr_max[0] = a[0] + max(prev_max[0], prev_max[1])
    curr_max[1] = a[1] + max(prev_max)
    curr_max[2] = a[2] + max(prev_max[1], prev_max[2])
    
    curr_min[0] = a[0] + min(prev_min[0], prev_min[1])
    curr_min[1] = a[1] + min(prev_min)
    curr_min[2] = a[2] + min(prev_min[1], prev_min[2])
    
    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))