import sys

def euclidean(X, Y):
    if Y == 0:
        return X

    a = max(X, Y)
    b = min(X, Y)
    p = 0

    if b == 0:
        return a

    while True:
        p = a % b

        if p == 0:
            break

        a = b
        b = p

    return b

aa, ab, ac, ad = map(int, sys.stdin.readline().split())
ba, bb, bc, bd = map(int, sys.stdin.readline().split())

rst = [[] for _ in range (4)]

if ac == 0 or ad == 0 :
    ac = 0
    ad = 0

if bc == 0 or bd == 0 : 
    bc = 0
    bd = 0

# times
a = aa*ba
b = ab*bb + ac*bc*ad
c = ac*bb + ab*bc

if c == 0 :
    d = 0
    gcd = euclidean(a, b)
    a //= gcd
    b //= gcd
    
else : 
    d = ad
    gcd = euclidean(a, b)
    gcd = euclidean(gcd, c)
    a //= gcd
    b //= gcd
    c //= gcd
    
if a < 0 : 
    a = abs(a)
    b = -1 * b
    c = -1 * c

times = [a, b, c, d]
rst[2] = times

# div 
a = aa**2 * bb**2 - aa**2 * bc**2 * bd
b = aa*ab*ba*bb - bd*aa*bc*ba*ac
c = ba*ac*aa*bb - aa*bc*ba*ab

if c == 0 :
    d = 0
    gcd = euclidean(a, b)
    a //= gcd
    b //= gcd
    
else : 
    d = ad
    gcd = euclidean(a, b)
    gcd = euclidean(gcd, c)
    a //= gcd
    b //= gcd
    c //= gcd
    
if a < 0 : 
    a = abs(a)
    b = -1 * b
    c = -1 * c

div = [a, b, c, d]
rst[3] = div

LCM = (aa * ba) // euclidean(aa, ba) # GCD-LCM way (for +, -)
ta = LCM // aa
tb = LCM // ba

# plus
a = ta*aa
b = ta*ab + tb*bb
c = ta*ac + tb*bc

if c == 0 :
    d = 0
    gcd = euclidean(a, b)
    a //= gcd
    b //= gcd
    
else : 
    d = ad
    gcd = euclidean(a, b)
    gcd = euclidean(gcd, c)
    a //= gcd
    b //= gcd
    c //= gcd
    
if a < 0 : 
    a = abs(a)
    b = -1 * b
    c = -1 * c
    
plus = [a, b, c, d]
rst[0] = plus

# minus
a = ta*aa
b = ta*ab - tb*bb
c = ta*ac - tb*bc

if c == 0 :
    d = 0
    gcd = euclidean(a, b)
    a //= gcd
    b //= gcd
    
else : 
    d = ad
    gcd = euclidean(a, b)
    gcd = euclidean(gcd, c)
    a //= gcd
    b //= gcd
    c //= gcd
    
if a < 0 : 
    a = abs(a)
    b = -1 * b
    c = -1 * c
    
minus = [a, b, c, d]
rst[1] = minus

for i in rst :
    print (*i)