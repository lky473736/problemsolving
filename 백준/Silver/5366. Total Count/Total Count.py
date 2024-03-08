import sys
from collections import defaultdict

dicta = dict()

while True :
    key = sys.stdin.readline().rstrip()
    
    if key == '0' :
        break
    
    if key in dicta.keys() :
        dicta[key] += 1
        
    else :
        dicta[key] = 1
        
suma = 0

for key in dicta.keys() :
    print (f'{key}: {dicta[key]}')
    suma += dicta[key]
    

print (f"Grand Total: {suma}")