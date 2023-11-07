''' b진수를 10진수로 변환하는 코드
xlist = list(str(x))[::-1]
print (xlist)
suma = 0
indices = 0

for i in xlist : 
    suma += int(i) * (b ** indices)
    indices += 1
    
print (suma)'''

x, b = map(int, input().split())
minus = 0
rest = 1
alist = []
blist = []

if b >= 0 : # 양의 진법
    if x < 0 : 
        x = abs(x)
        minus += 1
        
    while rest != 0 :
        alist.append(x // b)
        blist.append(x % b)
        
        rest = alist[-1]
        x = alist[-1]
    
    blist = [str(j) for j in blist][::-1]
    
    if alist[-1] != 0:
        if minus == 1 :
            print(-1 * int(str(alist[-1]) + "".join(blist)))
        
        else :
            print(int(str(alist[-1]) + "".join(blist)))
    else:
        if minus == 1 :
            print('-' + "".join(blist))
            
        else : 
            print("".join(blist))
            
        
else : # 음의 진법
    while rest != 0 :
        alist.append(x // b)
        if x % b < 0 : 
            alist[-1] = alist[-1] + 1
            blist.append(x - 1 * (b * alist[-1]))
            
        else :
            blist.append(x % b)
        
        rest = alist[-1]
        x = alist[-1]
    
    blist = [str(j) for j in blist][::-1]
    
    if alist[-1] != 0:
        print(int(str(alist[-1]) + "".join(blist)))
        
    else:
        print("".join(blist))