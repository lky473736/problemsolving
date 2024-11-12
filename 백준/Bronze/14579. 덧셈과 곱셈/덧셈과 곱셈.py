import sys

a, b = map(int, sys.stdin.readline().split())

# operand_1 = ((a-1) * a // 2) + (b - a + 1)
# operand_2 = 0
# cur = a

# for i in range (b - a + 1, 0, -1) :
#     operand_2 *= a * i
    
# print (operand_1 * operand_2)

rst = 1
for i in range (a, b + 1) : 
    sumation = i * (i+1) // 2
    rst *= sumation
    
print (rst % 14579)