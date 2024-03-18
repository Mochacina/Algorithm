# abs to max
n = int(input())
l = list(map(int, input().split()))
visited = [0] * n
ans = 0
def cal(l2=[]):
    global ans
    if len(l2) == n:
        temp = sum([abs(l2[i]-l2[i+1]) for i in range(n-1)]) 
        ans = max(ans, temp)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            cal(l2 + [l[i]])
            visited[i] = False
cal()
print(ans) 

# # abs to max
# n = int(input())
# l = list(map(int, input().split()))
# ans = 0
# def cal(l2=[]):
#     global ans
#     if len(l2)==n:
#         temp = sum([abs(l2[i]-l2[i+1]) for i in range(n-1)]) 
#         for i in range(n-1):
#             temp += abs(l2[i]-l2[i+1])
#         ans = max(ans, temp)
#         return
#     for i in range(n):
#         if l[i] not in l2: cal(l2+[l[i]])
# cal()
# print(ans) 