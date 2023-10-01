def testnum (A, B, C, D, E) :
    return (A**2 + B**2 + C**2 + D**2 + E**2) % 10
    
a, b, c, d, e = map(int, input().split())

print (testnum(a, b, c, d, e))
