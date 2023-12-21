x = int(input())
b = -2
minus = 0
rest = 1
alist = []
blist = []

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