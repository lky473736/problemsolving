import sys
import math

nlist = []

for _ in range (100) :
    compo = int(sys.stdin.readline())
    nlist.append (compo)
    
print ("ans : ", str(sum(nlist))[0:10])
