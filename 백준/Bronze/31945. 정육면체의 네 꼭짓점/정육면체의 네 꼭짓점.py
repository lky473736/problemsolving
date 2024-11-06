import sys

T = int(sys.stdin.readline())

seta = set()

for compo in [[0, 1, 2, 3], [0, 2, 4, 6], [4, 5, 6, 7], [1, 3, 5, 7], [0, 1, 4, 5], [2, 3, 6, 7]] : 
    strlist = [str(char) for char in compo]
    word = ''.join(strlist)
    seta.add(word)
    
# print (seta)

for i in range (T) :
    slist = list(map(str, sys.stdin.readline().split()))
    sword = ''.join (sorted(slist))
    
    if sword in seta : 
        print ("YES")
        
    else : 
        print ("NO")