# N, S, R = map(int, input().split())
# Sl = [0]*N
# Rl = [0]*N
# for i in list(map(int, input().split())): Sl[i-1] = 1
# for i in list(map(int, input().split())): Rl[i-1] = 1
# for i in range(N):
#     if Rl[i]==Sl[i]:Rl[i],Sl[i] = 0,0
# print(Sl, Rl)
# while sum(Rl) and sum(Sl):
#     left = 0
#     right = 9
#     for i in range(N):
#         if Sl[i]:left = i;break
#     for i in reversed(range(N)):
#         if Sl[i]:right = i;break
#     if left-1 >= 0 and Rl[left-1]:
#         Sl[left],Rl[left-1]=0,0
#     elif right+1 < N and Rl[right+1]:
#         Sl[right],Rl[right+1]=0,0
#     elif left+1 < N and Rl[left+1]:
#         Sl[left],Rl[left+1]=0,0
#     elif right-1 >= 0 and Rl[right-1]:
#         Sl[right],Rl[right-1]=0,0
# print(sum(Sl))

N,S,R = map(int, input().split())
kayak = [1]*N
for i in list(map(int, input().split())): kayak[i-1]-=1
for i in list(map(int, input().split())): kayak[i-1]+=1
for i in range(N):
    if not kayak[i]:
        if i-1 >= 0 and kayak[i-1] > 1:
            kayak[i-1],kayak[i] = 1,1
        elif i+1 < N and kayak[i+1] > 1:
            kayak[i+1],kayak[i] = 1,1
print(sum([1 for i in kayak if not i]))