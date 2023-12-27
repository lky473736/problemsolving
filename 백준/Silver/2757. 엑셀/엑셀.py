col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # 26 alphabets

# 26진법처럼 계산

while True :
    component = input()
    component = component[1:]
    compolist = component.split('C')
    
    rn = int(compolist[0])
    cn = int(compolist[1])
    
    if rn == 0 and cn == 0 :
        break
    
    cn -= 1
    formation_26 = []
    
    while cn >= 0 :
        n = cn % 26
        cn = (cn // 26) - 1

        formation_26.append(n)
        
    formation_26 = formation_26[::-1]
    for i in range (len(formation_26)) :
        formation_26[i] = col[formation_26[i]]
 
    print(''.join(formation_26) + str(rn))