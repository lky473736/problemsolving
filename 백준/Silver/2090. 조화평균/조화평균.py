import sys

def euclidean (X, Y) :
    a = Y 
    b = X % Y 
    p = 0
    
    if b == 0 :
        return a
    
    while True :
        p = a % b
        
        if p == 0 :
            break
        
        a = b
        b = p
        
    return b
    
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

if N == 1 :
    print (f'{lst[0]}/1')
    exit()

pref1 = lst[0] # 분모
pref2 = 1 # 분자

for i in range (N-1) : 
    # print (pref1, lst[i+1])
    
    lcm = pref1 * lst[i+1] // euclidean (pref1, lst[i+1])
    # print ("pref1, lst[i+1], lcm :", pref1, lst[i+1], lcm)
    
    if i == 0 : 
        pref2 = lcm // lst[0] + lcm // lst[i+1]
        
    else : 
        pref2 = pref2 * (lcm//pref1) + lcm // lst[i+1]
    
    # print ("pref2 :", pref2)
        
    pref1 = lcm
    
gcd = euclidean(pref1, pref2)
print (str(pref1 // gcd) + '/' + str(pref2 // gcd))