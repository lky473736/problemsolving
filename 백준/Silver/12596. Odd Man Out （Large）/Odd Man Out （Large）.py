import sys

N = int(sys.stdin.readline())

for i in range (N) :
    G = int(sys.stdin.readline())
    people = list(map(int, sys.stdin.readline().split()))
    counting = dict()
    
    for j in range (G) :
        try : 
            counting[people[j]] += 1
            
        except : 
            counting[people[j]] = 1
            
    for key in counting.keys() :
        if counting[key] == 1 :
            print (f"Case #{i+1}:", key)