K = int(input())

numlist = list()

for i in range (K) :
    num = int(input())
    
    if num == 0 :
        del numlist[-1]
        
    else : 
        numlist.append(num)
        
print (sum(numlist))