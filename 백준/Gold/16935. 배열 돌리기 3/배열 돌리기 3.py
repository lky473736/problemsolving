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

operations = list(map(int, sys.stdin.readline().split()))

for operation in operations :
    if operation == 1 : 
        slist = slist[::-1]
        
    elif operation == 2 : 
        for j in range (N) :
            slist[j] = slist[j][::-1]
    
    elif operation == 3 : 
        nlist = list()
        for j in range (M) :
            compo = list()
            for k in range (N) :
                compo.append (slist[N-1-k][j])
            nlist.append (compo)
        
        slist = nlist
        N, M = M, N
    
    elif operation == 4 : 
        nlist = list()
        for j in range (M) :
            compo = list()
            for k in range (N) :
                compo.append(slist[k][M-1-j])
            nlist.append (compo)
        
        slist = nlist
        N, M = M, N
    
    elif operation == 5 : 
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        
        # getting tempN
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[j][k])
            temp1.append (compo)
            
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[j][M//2 + k])
            temp2.append (compo)
        
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[N//2 + j][k])
            temp3.append (compo)
            
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[N//2 + j][M//2 + k])
            temp4.append (compo)
            
        # for temp in [temp1, temp2, temp3, temp4] :
        #     print (temp)
         
        temp = list()  
        for j in range (N//2) :
            temp.append (temp3[j] + temp1[j])
        
        for j in range (N//2) :
            temp.append (temp4[j] + temp2[j])
            
        slist = temp
    
    elif operation == 6 : 
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        
        # getting tempN
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[j][k])
            temp1.append (compo)
            
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[j][M//2 + k])
            temp2.append (compo)
        
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[N//2 + j][k])
            temp3.append (compo)
            
        for j in range (N//2) :
            compo = list()
            for k in range (M//2) :
                compo.append (slist[N//2 + j][M//2 + k])
            temp4.append (compo)
            
        # for temp in [temp1, temp2, temp3, temp4] :
        #     print (temp)
         
        temp = list()  
        for j in range (N//2) :
            temp.append (temp2[j] + temp4[j])
        
        for j in range (N//2) :
            temp.append (temp1[j] + temp3[j])
            
        slist = temp
    
    else : 
        pass
    
    # print ("\n operation #", operation);
    # for row in slist :
    #     print (*row)
    
# print ("\n ************************ \n")
for row in slist :
    print (*row)