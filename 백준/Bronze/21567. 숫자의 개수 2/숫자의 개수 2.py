A = int(input())
B = int(input())
C = int(input())

for i in range(10) :
    if str(i) in str(A * B * C) : 
        print (str(A * B * C).count(str (i)))
        
    else : 
        print (0)