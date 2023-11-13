# n, s = map(int,input().split())
# l = list(map(int,input().split()))

# list = []
# ans = []

# def dfs(a,b):
#     if len(list) == b and sum(list) == s:
#         if(set(list) not in ans): ans.append(set(list))
#         print(list)
#         return
#     for i in range(a,n):
#         if l[i] not in list:
#             list.append(l[i])
#             dfs(a+1,b)
#             list.pop()

# for j in range(1,n+1):dfs(0,j)
# print(len(ans))
    
# for i in range(n): # 숫자 몇개 고를지 for문
#     buf = []
#     for _ in range(i):
#         for j in range(n):


# def solve(idx, SUM):
#     print(idx, SUM)
#     global ans
#     if idx >= N:
#         return
#     SUM += nums[idx]
#     if SUM == S:
#         ans += 1
#     solve(idx + 1, SUM - nums[idx])
#     solve(idx + 1, SUM)

# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
# ans = 0
# solve(0, 0)
# print(ans)

def backtrack(a,b):
    global cnt
    if a >= n: return
    b += l[a]
    if b == s: cnt+=1
    backtrack(a+1, b)
    backtrack(a+1, b-l[a])

n, s = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0
backtrack(0,0)
print(cnt)