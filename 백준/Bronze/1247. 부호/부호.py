import sys

for testset in range (3) : 
    N = int(sys.stdin.readline())
    S = 0
    
    for i in range (N) :
        compo = int(sys.stdin.readline())
        S += compo
        
    if S > 0 :
        print ("+")
        
    elif S < 0 :
        print ("-")
        
    else :
        print ("0")