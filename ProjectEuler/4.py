import sys
import math

palindrome = []

for i in range (100, 1000) : 
    for j in range (100, 1000) : 
        compo = str(i * j)
        length = len(compo)
        
        if length % 2 == 0 : 
            if compo[0:length//2][::-1] == compo[length//2:] :
                palindrome.append (int(compo))
            
        else : 
            if compo[0:length//2][::-1] == compo[length//2+1:] :
                palindrome.append (int(compo))
                
print (sorted(palindrome))
