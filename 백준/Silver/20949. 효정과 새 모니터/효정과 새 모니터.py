import sys
import math

N = int(sys.stdin.readline())

PPI = list()

for i in range (N) :
    W, H = map(int, sys.stdin.readline().split())
    
    PPI.append([math.sqrt(W**2 + H**2) / 77, i+1])
    
PPI = sorted(PPI, key = lambda x : (x[0], -x[1]), reverse = True)

for compo in PPI :
    print (compo[1])