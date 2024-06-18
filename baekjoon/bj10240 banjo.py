import math
import sys

EPSILON = 1e-9
TWOPI = 2 * math.pi
STEP = 3

# �� ���� ���̸� �޾� �ﰢ���� ���̸� ���ϴ� �Լ�
# a,b = ������ ������ ���� ����
# c = ������ �ݴ�Ǵ� ���� ����
def angle(a, b, c):
    return math.acos((a*a + b*b - c*c) / (2.0 * a * b))

# �� ���� ���̿� ������ �־����� �� ������ ���� ���̸� ���ϴ� �Լ�
def length(a, b, theta):
    return math.sqrt(a*a + b*b - 2.0 * a * b * math.cos(theta))

# �־��� ������ 0�� 2�� ������ ������ ��ȯ
def positive(angle):
    while angle < 0.0: angle += TWOPI
    while angle >= TWOPI: angle -= TWOPI
    return angle

# �־��� ������ 0�� �� ������ ������ ��ȯ
def normalize(angle):
    angle = positive(angle)
    if angle > math.pi:
        angle = TWOPI - angle
    return angle

def lava(angle):
    distance = 0.0
    if (t==0):
        # t�� 0�� ��� ��Ͽ� �� �� �����Ƿ� ������ �ѷ��� ���� �ɾ����
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
    
    # �� A, B, C ������ �Ÿ� ���
    dAB = math.hypot(xB - xA, yB - yA)
    dAC = math.hypot(xC - xA, yC - yA)
    dBC = math.hypot(xC - xB, yC - yB)
    
    # �ּ�ȭ�� ����� �Լ��� ����
    def min_b(x,y):
        return length(r, dAC, normalize(x - aCA)) + length(r, dBC, normalize(y - aCB)) + lava(normalize(y - x)) 

    def min_a(x,y):
        return minimize(loB, hiB, y, min_b)
    
    # ���� ��� Ȯ��
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
            # �� A, B, C�� ���� �� ���� ���� ���
            cross = 2.0*math.sqrt( r*r-dCP*dCP ) # ���� ���������� �Ÿ� ���
            if cross<t: minDist = dAB
    
    if minDist < -0.5:
        at = angle(r, r, t)

        # �߽� C���� �� A �� B������ ����
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