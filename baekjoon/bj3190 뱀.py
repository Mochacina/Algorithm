#print(l, apples, rotate)

# n = int(input())+1
# l = [[0]*n for _ in range(n)]
# apples = [list(map(int, input().split()))for _ in range(int(input()))]
# rotate = [list(input().split())for i in range(int(input()))][::-1]
# turn=1;level=1
# cor = [1,1]
# direction = [[0,1],[-1,0],[0,-1],[1,0]];n_dir=0
# l[1][1] = 1
# while 1:
#     if len(rotate) > 0:
#         if int(rotate[-1][0])+1 == turn:
#             _,m = rotate.pop()
#             n_dir += 1 if m == 'L' else -1
#             n_dir = (n_dir+4)%4
#     turn += 1
#     y,x = direction[n_dir]
#     cor[0] += y
#     cor[1] += x
#     if cor[0] <= 0 or cor[0] >= n or cor[1] <= 0 or cor[1] >= n: break
#     if cor in apples:
#         level += 1
#         del apples[apples.index(cor)]
#     #print(turn, level)
#     if turn-level > l[cor[0]][cor[1]] or l[cor[0]][cor[1]]==0:
#         l[cor[0]][cor[1]] = turn
#         #for node in l:print(node)
#     else: break
# print(turn-1)

n = int(input())+1
l = [[0]*n for _ in range(n)]
apples=[list(map(int, input().split()))for _ in range(int(input()))]
rotate=[list(input().split())for i in range(int(input()))][::-1]
turn=1;level=1
cor=[1,1]
direction = [[0,1],[-1,0],[0,-1],[1,0]];n_dir=0
l[1][1] = 1
while 1:
    if len(rotate) > 0:
        if int(rotate[-1][0])+1 == turn:
            _,m = rotate.pop()
            n_dir += 1 if m == 'L' else -1
            n_dir = (n_dir+4)%4
    turn += 1
    y,x = direction[n_dir]
    cor[0] += y
    cor[1] += x
    if cor[0] <= 0 or cor[0] >= n or cor[1] <= 0 or cor[1] >= n: break
    if cor in apples:
        level += 1
        del apples[apples.index(cor)]
    if turn-level > l[cor[0]][cor[1]] or not l[cor[0]][cor[1]]:
        l[cor[0]][cor[1]] = turn
    else: break
print(turn-1)