# import sys
# input = sys.stdin.readline

# def find(n):
    # if n == 1: return 0
    
    # l = 2
    # r = 2
    # sum = 2
    # cnt = 0
    
    # while l <= n:
    #     if sum == n:
    #         cnt += 1
    #         r += 1
    #         sum += r
    #     elif sum < n:
    #         r += 1
    #         sum += r
    #     else:
    #         sum -= l
    #         l += 1
    
    # return cnt
    # count = 0
    # for start in range(1, n+1):
    #     total = 0
    #     for end in range(start, n + 1):
    #         total += end
    #         if total == n:
    #             count += 1
    #             break
    #         elif total > n:
    #             break
    # return count

# while n:=int(input()): print(find(n))

# import sys
# input = sys.stdin.readline

# m = 1000000
# l = [0]*(m+1)
# left = 2
# right = 2
# current_sum = 2

# while left <= m:
#     if current_sum <= m:
#         l[current_sum] += 1
#         right += 1
#         current_sum += right
#     else:
#         current_sum -= left
#         left += 1

# while n:=int(input()): print(l[n])

# import sys
# input = sys.stdin.readline

# m = 1000000
# l = [0]*(m+1)
# for i in range(2,m):
#     s = 0
#     for j in range(i,m):
#         s += j
#         if s > m: break
#         l[s] += 1

# while n:=int(input()): print(l[n])

t=0
l=[0,0]+[1]*999999
for i in range(2,1414):
 t+=i-1
 for j in range(2,(1000000-t)//i+1):l[i*j+t]+=1
while n:=int(input()):print(l[n])