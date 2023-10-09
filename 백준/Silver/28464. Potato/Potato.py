N = int(input())

potato = list(map(int, input().split()))

sung = 0

'''park = 0
sung = 0

while True :
    potato.sort()
    
    park += potato[-1]
    
    del potato[-1]
    if potato == [] :
        break
    
    sung += potato[0]
    
    del potato[0]
    if potato == [] :
        break
    
print (sung, park)
'''

potato.sort()

if len(potato) % 2 == 0 :
    for i in range (len(potato) // 2) :
        sung += potato[i]
        
else :
    for i in range (len(potato) // 2) :
        sung += potato[i]
        
print (sung, sum(potato) - sung)