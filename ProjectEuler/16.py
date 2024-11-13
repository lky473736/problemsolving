import sys
import math

num = 1

for i in range (1, 1001) :
    print (num)
    num *= 2
    
print ("final :", num)
charlist = list(str(num))

rst = 0
for char in charlist : 
    rst += int(char)
    
print ("rst : ", rst)
