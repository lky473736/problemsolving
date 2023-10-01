T = int(input()) 

R_list = []
S_list = []

for i in range (T) :
    R, S = input().split()
    R = int(R)
    
    R_list.append (R)
    S_list.append (S)

for j in range (len(S_list)) :
    '''for k in range (len(S_list[j])) :
        print (S_list[j][k] * R_list[j], end = '')
        
    print ('\n')'''
    
    result = ""
    
    for k in range(len(S_list[j])):
        result += S_list[j][k] * R_list[j]
        
    print(result)
