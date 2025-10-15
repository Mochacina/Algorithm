import math
import sys

EPSILON = 1e-9
TWOPI = 2 * math.pi
STEP = 3

# 세 변의 길이를 받아 삼각형의 길이를 구하는 함수
# a,b = 각도에 인접한 변의 길이
# c = 각도와 반대되는 변의 길이
def angle(a, b, c):
    return math.acos((a*a + b*b - c*c) / (2.0 * a * b))

# 두 변의 길이와 각도가 주어졌을 때 나머지 변의 길이를 구하는 함수
def length(a, b, theta):
    return math.sqrt(a*a + b*b - 2.0 * a * b * math.cos(theta))

# 주어진 각도를 0과 2π 사이의 값으로 변환
def positive(angle):
    while angle < 0.0: angle += TWOPI
    while angle >= TWOPI: angle -= TWOPI
    return angle

# 주어진 각도를 0과 π 사이의 값으로 변환
def normalize(angle):
    angle = positive(angle)
    if angle > math.pi:
        angle = TWOPI - angle
    return angle

def lava(angle):
    distance = 0.0
    if (t==0):
        # t가 0인 경우 용암에 들어갈 수 없으므로 무조건 둘레를 따라 걸어야함
        distance = r * angle
    else:
        ts = math.floor(angle/at)
        distance = ts*t + length(r,r, angle-ts*at)
    return distance

def minimize(lo, hi, x, func):
    minimum = float('inf')
    while abs(hi - lo) > EPSILON:
        increment = (hi - lo) / STEP
        minimum = float('inf')
        where = 0
        for i in range(STEP + 1):
            y = lo + i * increment
            v = func(x, y)
            if v < minimum:
                where = i
                minimum = v
        if where < STEP - 1:
            hi = lo + (where + 1) * increment
        if where > 1:
            lo = lo + (where - 1) * increment
    return minimum

def solve_banjo(xA, yA, xB, yB, xC, yC, r, t):
    global at
    minDist = -1.0
    
    # 점 A, B, C 사이의 거리 계산
    dAB = math.hypot(xB - xA, yB - yA)
    dAC = math.hypot(xC - xA, yC - yA)
    dBC = math.hypot(xC - xB, yC - yB)
    
    # 최소화에 사용할 함수들 정의
    def min_b(x,y):
        return length(r, dAC, normalize(x - aCA)) + length(r, dBC, normalize(y - aCB)) + lava(normalize(y - x)) 

    def min_a(x,y):
        return minimize(loB, hiB, y, min_b)
    
    # 직선 경로 확인
    if( abs( dAB + dBC - dAC ) < EPSILON ): minDist = dAB
    elif( abs( dAB + dAC - dBC ) < EPSILON ): minDist = dAB
    elif( abs( dAC + dBC - dAB ) < EPSILON ): 
        if r+r<t:
            minDist = dAB
    else:
        aBAC = angle( dAB, dAC, dBC )
        dCP = math.sin( aBAC ) * dAC
        dAP = math.sqrt( dAC*dAC - dCP*dCP )
        dBP = math.sqrt( dBC*dBC - dCP*dCP )
        if( dCP>=r or dAP>dAB or dBP>dAB ): minDist = dAB
        else:
            # 점 A, B, C가 직선 상에 있지 않은 경우
            cross = 2.0*math.sqrt( r*r-dCP*dCP ) # 원을 가로지르는 거리 계산
            if cross<t: minDist = dAB
    
    if minDist < -0.5:
        at = angle(r, r, t)

        # 중심 C에서 점 A 및 B까지의 각도
        aCA = positive(math.atan2(yA - yC, xA - xC))
        aCB = positive(math.atan2(yB - yC, xB - xC))
        
        loA = aCA
        diff = positive( math.acos( r / dAC ) )
        up = positive( loA+diff )
        dn = positive( loA-diff )
        diffA = hiA = up if normalize(aCB - up) < normalize(aCB - dn) else dn
        if( positive(hiA-loA) > math.pi ):
            t = loA
            loA = hiA
            hiA = t
        if( hiA>loA and hiA-loA > math.pi ): loA += TWOPI
        if( hiA<loA and loA-hiA > math.pi ): hiA += TWOPI
        
        loB = aCB
        diff = positive( math.acos( r / dBC ) )
        up = positive( loB+diff )
        dn = positive( loB-diff )
        
        hiB = up if normalize(diffA-up) < normalize(diffA-dn) else dn
        if( positive(hiB-loB) > math.pi ):
            t = loB
            loB = hiB
            hiB = t
        if( hiB>loB and hiB-loB > math.pi ): loB += TWOPI
        if( hiB<loB and loB-hiB > math.pi ): hiB += TWOPI
        
        return minimize(loA, hiA, 0, min_a)
    
    else: return minDist

input = sys.stdin.readline
while sum(data:=[*map(int,input().split())]):
    xA = int(data[0])
    yA = int(data[1])
    xB = int(data[2])
    yB = int(data[3])
    xC = int(data[4])
    yC = int(data[5])
    r = int(data[6])
    t = int(data[7])
    at = 0
    result = solve_banjo(xA, yA, xB, yB, xC, yC, r, t)
    print(f"{result:.2f}")

# short code version
# from math import*
# E=1e-9
# P=pi*2
# S=3
# def g(a,b,c):return acos((a*a+b*b-c*c)/(2*a*b))
# def l(a,b,t):return sqrt(a*a+b*b-2*a*b*cos(t))
# def p(a):
#  while a<0:a+=P
#  while a>=P:a-=P
#  return a
# def n(a):
#  a=p(a)
#  return P-a if a>pi else a
# def L(a):return r*a if t==0else int(a/at)*t+l(r,r,a-int(a/at)*at)
# def m(o,h,x,f):
#  while abs(h-o)>E:
#   i=(h-o)/S;v=1e9;w=0
#   for j in range(S+1):
#    y=o+j*i;u=f(x,y)
#    if u<v:w=j;v=u
#   if w<S-1:h=o+(w+1)*i
#   if w>1:o+=(w-1)*i
#  return v
# while 1:
#  d=[*map(int,input().split())]
#  if sum(d)==0:break
#  x,y,X,Y,u,v,r,t=d
#  a=hypot(X-x,Y-y);c=hypot(u-x,v-y);b=hypot(u-X,v-Y);M=-1
#  if abs(a+b-c)<E or abs(a+c-b)<E:M=a
#  elif abs(c+b-a)<E:M=a if r+r<t else M
#  else:
#   z=g(a,c,b);j=sin(z)*c;o=sqrt(c*c-j*j);q=sqrt(b*b-j*j)
#   if j>=r or o>a or q>a:M=a
#   else:
#    w=2*sqrt(r*r-j*j)
#    if w<t:M=a
#  if M<0:
#   at=g(r,r,t)
#   A=p(atan2(y-v,x-u));B=p(atan2(Y-v,X-u))
#   o=A;i=acos(r/c);U=p(o+i);D=p(o-i);F=d=U if n(B-U)<n(B-D)else D
#   if p(d-o)>pi:o,d=d,o
#   if d>o and d-o>pi:o+=P
#   if d<o and o-d>pi:d+=P
#   f=B;i=acos(r/b);U=p(f+i);D=p(f-i);h=U if n(F-U)<n(F-D)else D
#   if p(h-f)>pi:f,h=h,f
#   if h>f and h-f>pi:f+=P
#   if h<f and f-h>pi:h+=P
#   def G(x,y):return l(r,c,n(x-A))+l(r,b,n(y-B))+L(n(y-x))
#   def H(x,y):return m(f,h,y,G)
#   M=m(o,d,0,H)
#  print(f"{M:.2f}")