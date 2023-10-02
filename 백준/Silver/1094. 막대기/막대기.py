# 2진법으로 생각하면 됨

binary = [1, 2, 4, 8, 16, 32, 64]

X = int(input())

if X in binary : 
    print (1)
    exit()
    
else :
    print(str(bin(X)).count('1'))