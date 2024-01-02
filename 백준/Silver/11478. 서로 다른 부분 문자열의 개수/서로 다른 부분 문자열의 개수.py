S = input()
length = len(S)

if length == 1 :
    print (1)
    exit()
    
string = set()
k = length
i = 0
    
while i != length :
    for j in range (k) : 
        string.add(S[j : j+i+1])
        
    k -= 1
    i += 1
    
print (len(string))