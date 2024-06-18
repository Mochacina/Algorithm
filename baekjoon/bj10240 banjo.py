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