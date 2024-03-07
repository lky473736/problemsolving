import sys

N = int(sys.stdin.readline())

'''num_dict = dict()

for num in range (N) :
    num_dict[num + 1] = 0'''
    
A = sys.stdin.readline().rstrip()

suma = 0
sum_original = N * (N - 1) // 2
o = ''

for c in A :
    if c.isdigit() :
        o += c
        
    else :
        suma += int(o)
        o = ''
        
    '''if compo == ' ' :
        pass
    
    else :
        suma += int(compo)'''

    '''num_dict[int(compo)] += 1
    
    if num_dict[int(compo)] == 2 :
        print (compo)
        exit()'''
        
suma += int(o)
        
print (suma - sum_original)