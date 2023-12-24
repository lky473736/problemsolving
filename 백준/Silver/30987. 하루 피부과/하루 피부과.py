x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def F(x, a, b, c, d, e) :
    return 1/3 * a * (x**3) + 1/2* (b-d) * (x**2) + (c-e) * x 

print (round(F(x2, a, b, c, d, e) - F(x1, a, b, c, d, e)))