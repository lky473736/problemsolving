import sys

N = int(sys.stdin.readline())

log = set()

# 짝수 : 1
# 홀수 : 2

temp = ""
t = 1

for i in range (N) :
    word = sys.stdin.readline().rstrip()
    
    if i == 0 :
        log.add (word)
        temp = word
        continue
    
    if temp[-1] == word[0] and word not in log :
        log.add(word)
        temp = word
        pass
        
    else :
        t = 0 
    
    if t == 0 :
        if i % 2 == 0 : # 1
            print ("Player 1 lost")
            exit()
            
        else : # 2
            print ("Player 2 lost")
            exit()
        
print ("Fair Game")