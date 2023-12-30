import itertools
import sys

k = int(sys.stdin.readline())
inequ = list(sys.stdin.readline().rsplit())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

mina = '9999999999'
maxa = '0'

for compo in itertools.permutations(num, k+1) :
    finder = ""
    
    for i in range (k) : 
        '''if eval(compo[i] + inequ[i] + compo[i+1]) == False :
            break'''

        if inequ[i] == '<' : 
            if compo[i] > compo[i+1] : 
                break
            
        else :
            if compo[i] < compo[i+1] : 
                break
    
    else :     
        out = "".join(compo)
            
        if int(out) < int(mina) : 
            mina = out
                
        else :
            if int(out) > int(maxa) :
                maxa = out
        
print (maxa)
print (mina)

'''import itertools
import sys

k = int(sys.stdin.readline())
inequ = list(sys.stdin.readline().rsplit())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

rst = []

for compo in itertools.permutations(num, k+1) :
    for i in range (k) : 
        if inequ[i] == '<' : 
            if compo[i] > compo[i+1] : 
                break
            
        else :
            if compo[i] < compo[i+1] : 
                break
    else :    
        rst.append (compo)
    
rst.sort()
print (''.join(map(str, rst[-1])))
print (''.join(map(str, rst[0])))'''