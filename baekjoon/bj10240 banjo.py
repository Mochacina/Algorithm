import math
import sys

EPSILON = 1e-9
TWOPI = 2 * math.pi
STEP = 3

def angle(a, b, c):
    return math.acos((a*a + b*b - c*c) / (2.0 * a * b))

def length(a, b, theta):
    return math.sqrt(a*a + b*b - 2.0 * a * b * math.cos(theta))

def positive(angle):
    while angle < 0.0:
        angle += TWOPI
    while angle >= TWOPI:
        angle -= TWOPI
    return angle

def normalize(angle):
    angle = positive(angle)
    if angle > math.pi:
        angle = TWOPI - angle
    return angle

def lava(angle):
    distance = 0.0
    if (t==0):
        distance = r * angle
    else:
        ts = math.floor(angle/at)
        distance = ts*t + length(r,r, angle-ts+at)
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

def process_test_case(xA, yA, xB, yB, xC, yC, r, t):
    global at, mindist
    dAB = math.hypot(xB - xA, yB - yA)
    dAC = math.hypot(xC - xA, yC - yA)
    dBC = math.hypot(xC - xB, yC - yB)
    at = angle(r, r, t) if t > 0 else 0
    
    
    if( abs( dAB + dBC - dAC ) < EPSILON ): mindist = dAB
    elif( abs( dAB + dAC - dBC ) < EPSILON ): mindist = dAB
    elif( abs( dAC + dBC - dAB ) < EPSILON ): 
        if(r+r<t): mindist = dAB
    else:
        aBAC = angle( dAB, dAC, dBC )
        dCP = math.sin( aBAC ) * dAC
        dAP = math.sqrt( dAC*dAC - dCP*dCP )
        dBP = math.sqrt( dBC*dBC - dCP*dCP )
        if( dCP>=r or dAP>dAB or dBP>dAB ): mindist = dAB
        else:
            cross = 2.0*math.sqrt( r*r-dCP*dCP )
            if cross<t: mindist = dAB
    if mindist < -0.5:
        at = angle(r, r, t)

    # Angles from center C to points A and B
    aCA = positive(math.atan2(yA - yC, xA - xC))
    aCB = positive(math.atan2(yB - yC, xB - xC))

    # Define functions for minimization
    def min_b(x, y):
        return length(r, dAC, normalize(x - aCA)) + length(r, dBC, normalize(y - aCB)) + r * normalize(y - x)

    def min_a(x):
        return minimize(0, TWOPI, x, min_b)

    # Minimize over angle from A
    return minimize(0, TWOPI, 0, min_a)

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
    #if r == 0:break
    at = 0
    mindist = -1.0
    result = process_test_case(xA, yA, xB, yB, xC, yC, r, t)
    print(f"{result:.2f}")

