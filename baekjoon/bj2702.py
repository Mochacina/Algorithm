def gcd(x,y):
    l=[x,y]
    while min(l): l[l.index(max(l))] %= min(l)
    return max(l)
def lcm(x,y): return x*y//gcd(x,y)
def e6(x,y): print(f"{lcm(x,y)} {gcd(x,y)}")
    
for _ in range(int(input())):
    e6(*map(int, input().split()))