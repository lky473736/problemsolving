import sys 

n = int(input())

rst = 0
Alist = list()
Blist = list()
Clist = list()
Dlist = list() 

for i in range (n) :
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    Alist.append (a)
    Blist.append (b)
    Clist.append (c)
    Dlist.append (d)

aplusb = dict()
# keys = set()

for compo_a in Alist : 
    for compo_b in Blist :
        plus1 = compo_a + compo_b
        
        if plus1 not in aplusb : 
            aplusb[plus1] = 1 
            # keys.add(plus1)
            
        else :
            aplusb[plus1] += 1

for compo_c in Clist :
    for compo_d in Dlist :
        plus2 = -(compo_c + compo_d)
        
        if plus2 in aplusb :
            rst += aplusb[plus2]
            # rst += 1

print (rst)