import sys
import math

'''
6 6 1
1 6 2 9 8 4
7 2 6 9 8 2
1 8 3 4 2 9
7 4 6 2 3 1
9 2 3 6 1 5
4 2 9 3 1 8
'''

N, M, R = map(int, sys.stdin.readline().split())

slist = []

for i in range (N) :
    row = list(map(int, sys.stdin.readline().split()))
    slist.append(row)

for i in range (R) :
    operation = int(sys.stdin.readline())
    
    if operation == 1 : 
        slist = slist[::-1]
        
    elif operation == 2 : 
        for j in range (M) :
            slist[j] = slist[j][::-1]
    
    elif operation == 3 : 
        nlist = list()
        for j in range (M) :
            compo = list()
            for k in range (N) :
                compo.append(slist[N-1-k][j])
            nlist.append (compo)
        
        slist = nlist
    
    elif operation == 4 : 
        nlist = list()
        for j in range (M) :
            compo = list()
            for k in range (N) :
                compo.append(slist[k][M-1-j])
            nlist.append (compo)
        
        slist = nlist
    
    elif operation == 5 : 
        temp = []
        
        # 1->2
        for j in range (N//2) :
            for k in range (M//2) :
                temp.append ()
    
    elif operation == 6 : 
        pass
    
    else : 
        pass
    
for row in range (N) :
    print (*slist[row])
