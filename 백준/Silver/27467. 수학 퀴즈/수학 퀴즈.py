import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

plst = []
qlst = []

for compo in lst :
    if compo <= 2 :
        if compo == 0 :
            qlst.append (1)
            
        elif compo == 1 : 
            plst.append (1)
            
        elif compo == 2 :
            plst.append (-1)
            qlst.append (-1)
            
    else :
        if compo % 3 == 0 :
            qlst.append (-1)
            
        elif compo % 3 == 1 :
            plst.append (-1)
            
        else :
            plst.append (1)
            qlst.append (1)
            
print (sum(plst), sum(qlst))