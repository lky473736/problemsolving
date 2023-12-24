import sys

N = int(sys.stdin.readline())

namelist = []

for _ in range (N) : 
    namelist.append(sys.stdin.readline().rstrip())
    
increase = sorted(namelist)
decrease = sorted(namelist, reverse = True)

if increase == namelist :
    print ("INCREASING")
    
elif decrease == namelist : 
    print ("DECREASING")
    
else :
    print ("NEITHER")