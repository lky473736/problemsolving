finder = list()

per = 0

for i in range (10) :
    outer, inner = map(int, input().split())
    
    per -= outer
    finder.append (per)
    
    per += inner
    finder.append (per)
    
print (max(finder))