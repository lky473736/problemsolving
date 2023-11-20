N = list(input())
# 0~9
set = 1

current_set = [str(i) for i in range (10)]

for compo in N :
    if compo == '6' and compo not in current_set and '9' in current_set : 
        current_set.remove('9')
        
    elif compo == '9' and compo not in current_set and '6' in current_set : 
        current_set.remove('6')
        
    elif compo in current_set :
        current_set.remove(compo)
        
    else :
        set += 1
        
        for i in range (10) :
            current_set.append (str(i))
            
        current_set.remove(compo)
    
print (set)