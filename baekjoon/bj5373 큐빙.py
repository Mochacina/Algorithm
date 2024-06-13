from collections import deque

r = range
def cubing(d,v):
    l,l2 = dic[d],dic2[d]
    dq = deque([cube[i] for i in l])
    dq2 = deque([cube[i] for i in l2])
    dq.rotate(3*v)
    dq2.rotate(2*v)
    for i in l:cube[i] = dq.popleft()
    for i in l2:cube[i] = dq2.popleft()

dic = {
    'U':[38,37,36,29,28,27,20,19,18,11,10,9],
    'D':[15,14,13,24,23,22,33,32,31,42,41,40],
    'L':[0,7,6,18,25,24,45,52,51,40,39,38],
    'R':[49,48,47,22,21,20,4,3,2,36,43,42],
    'B':[2,1,0,9,16,15,51,50,49,31,30,29],
    'F':[6,5,4,27,34,33,47,46,45,13,12,11]
}

dic2 = {
    'U':[*r(8)],
    'D':[*r(45,53)],
    'L':[*r(9,17)],
    'R':[*r(27,35)],
    'B':[*r(36,44)],
    'F':[*r(18,26)]
}

for _ in range(int(input())):
    cube = list('w'*9+'g'*9+'r'*9+'b'*9+'o'*9+'y'*9)
    n = int(input())
    for i in [*input().split()]:
        cubing(i[0],[-1,1][i[1]=='+'])
    for i in [[0,1,2],[7,8,3],[6,5,4]]:
        print(''.join([cube[j] for j in i]))

"""
         0  1  2 
         7  8  3 
         6  5  4 
9  10 11 18 19 20 27 28 29 36 37 38
16 17 12 25 26 21 34 35 30 43 44 39
15 14 13 24 23 22 33 32 31 42 41 40
         45 46 47
         52 53 48
         51 50 49
"""